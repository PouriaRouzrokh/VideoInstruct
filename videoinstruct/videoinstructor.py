import os
import time
from typing import List, Optional, Dict, Any, Union, Tuple, ClassVar
from pydantic import BaseModel, Field
import json
import re

from videoinstruct.agents.VideoInterpreter import VideoInterpreter, VideoInterpreterConfig
from videoinstruct.agents.DocGenerator import DocGenerator, DocGeneratorConfig
from videoinstruct.utils.transcription import transcribe_video


class ResponseType(BaseModel):
    """Enum-like class for response types from DocGenerator."""
    DOCUMENTATION: ClassVar[str] = "documentation"
    QUESTION: ClassVar[str] = "question"
    COMPLETE: ClassVar[str] = "complete"


class DocGeneratorResponse(BaseModel):
    """Structured response from DocGenerator."""
    type: str  # One of ResponseType values
    content: str  # Documentation content or question
    confidence: Optional[float] = None  # Confidence level (0-1) if applicable


class VideoInstructorConfig(BaseModel):
    """Configuration for the VideoInstructor class."""
    doc_generator_config: Optional[DocGeneratorConfig] = None
    video_interpreter_config: Optional[VideoInterpreterConfig] = None
    max_iterations: int = Field(default=10)
    user_feedback_interval: int = Field(default=5)
    output_dir: str = Field(default="output")
    temp_dir: str = Field(default="temp")


class VideoInstructor:
    """
    A class that orchestrates the workflow between DocGenerator and VideoInterpreter.
    
    This class handles:
    1. Video transcription extraction
    2. Passing transcription to DocGenerator
    3. Managing the Q&A flow between DocGenerator and VideoInterpreter
    4. Collecting user feedback and refining documentation
    """
    
    def __init__(
        self,
        video_path: Optional[str] = None,
        transcription_path: Optional[str] = None,
        doc_generator_api_key: Optional[str] = None,
        video_interpreter_api_key: Optional[str] = None,
        config: Optional[VideoInstructorConfig] = None
    ):
        """
        Initialize the VideoInstructor.
        
        Args:
            video_path: Path to the video file.
            transcription_path: Path to an existing transcription file (optional).
            doc_generator_api_key: API key for the DocGenerator's LLM provider.
            video_interpreter_api_key: API key for the VideoInterpreter (Gemini).
            config: Configuration for the VideoInstructor.
        """
        self.video_path = video_path
        self.transcription_path = transcription_path
        self.transcription = None
        self.config = config or VideoInstructorConfig()
        
        # Create output and temp directories if they don't exist
        if not os.path.exists(self.config.output_dir):
            os.makedirs(self.config.output_dir)
        if not os.path.exists(self.config.temp_dir):
            os.makedirs(self.config.temp_dir)
        
        # Initialize DocGenerator
        self.doc_generator = DocGenerator(
            api_key=doc_generator_api_key,
            config=self.config.doc_generator_config,
            output_dir=self.config.output_dir
        )
        
        # Initialize VideoInterpreter
        self.video_interpreter = VideoInterpreter(
            api_key=video_interpreter_api_key,
            config=self.config.video_interpreter_config
        )
        
        # Load video and transcription if provided
        if video_path:
            self.load_video(video_path)
            
        if transcription_path:
            self.load_transcription(transcription_path)
    
    def load_video(self, video_path: str) -> None:
        """
        Load a video file and extract its transcription.
        
        Args:
            video_path: Path to the video file.
        """
        print(f"Loading video from {video_path}...")
        self.video_path = video_path
        
        # Load video into VideoInterpreter
        self.video_interpreter.load_video(video_path)
        
        # Extract transcription if not already provided
        if not self.transcription:
            self._extract_transcription()
    
    def load_transcription(self, transcription_path: str) -> None:
        """
        Load an existing transcription file.
        
        Args:
            transcription_path: Path to the transcription file.
        """
        print(f"Loading transcription from {transcription_path}...")
        self.transcription_path = transcription_path
        
        try:
            with open(transcription_path, 'r') as file:
                self.transcription = file.read()
            
            # Set transcription in DocGenerator
            if self.transcription:
                self.doc_generator.set_transcription(self.transcription)
                print("Transcription loaded successfully.")
        except Exception as e:
            print(f"Error loading transcription: {str(e)}")
    
    def _extract_transcription(self) -> None:
        """Extract transcription from the loaded video."""
        if not self.video_path:
            raise ValueError("No video loaded. Please load a video first.")
        
        # Generate a default transcription path if not provided
        if not self.transcription_path:
            video_name = os.path.splitext(os.path.basename(self.video_path))[0]
            self.transcription_path = os.path.join(self.config.output_dir, f"{video_name}_transcription.txt")
        
        # Check if transcription file already exists
        if os.path.exists(self.transcription_path):
            print(f"Transcription file already exists at {self.transcription_path}. Loading existing transcription...")
            self.load_transcription(self.transcription_path)
            return
        
        print("Extracting transcription from video...")
        
        # Extract transcription using the utility function
        success = transcribe_video(
            video_path=self.video_path,
            output_path=self.transcription_path,
            temp_path=self.config.temp_dir
        )
        
        if success:
            # Load the transcription
            with open(self.transcription_path, 'r') as file:
                self.transcription = file.read()
            
            # Set transcription in DocGenerator
            self.doc_generator.set_transcription(self.transcription)
            print(f"Transcription extracted and saved to {self.transcription_path}")
        else:
            raise ValueError("Failed to extract transcription from video.")
    
    def _get_structured_response(self, response: str) -> DocGeneratorResponse:
        """
        Parse the response from DocGenerator to determine if it's a question or documentation.
        
        Args:
            response: The response from DocGenerator.
            
        Returns:
            A DocGeneratorResponse object with the type and content.
        """
        # Check if the response is in JSON format
        try:
            # Try to parse as JSON
            json_response = json.loads(response)
            if isinstance(json_response, dict) and "type" in json_response and "content" in json_response:
                return DocGeneratorResponse(**json_response)
        except json.JSONDecodeError:
            pass
        
        # If not JSON, use heuristics to determine if it's a question or documentation
        # Look for question patterns
        question_patterns = [
            r'\?\s*$',  # Ends with question mark
            r'^(?:can|could|what|when|where|which|who|why|how)',  # Starts with question word
            r'I need more information about',
            r'Please provide more details',
            r'Can you clarify',
        ]
        
        for pattern in question_patterns:
            if re.search(pattern, response, re.IGNORECASE):
                return DocGeneratorResponse(type=ResponseType.QUESTION, content=response)
        
        # If it contains markdown headers, it's likely documentation
        if re.search(r'^#\s+', response, re.MULTILINE):
            return DocGeneratorResponse(type=ResponseType.DOCUMENTATION, content=response)
        
        # Default to documentation
        return DocGeneratorResponse(type=ResponseType.DOCUMENTATION, content=response)
    
    def _get_user_feedback(self, documentation: str) -> Tuple[str, bool]:
        """
        Get feedback from the user about the documentation.
        
        Args:
            documentation: The documentation to get feedback on.
            
        Returns:
            A tuple of (feedback, is_satisfied)
        """
        print("\n" + "="*50)
        print("CURRENT DOCUMENTATION:")
        print("="*50)
        print(documentation)
        print("\n" + "="*50)
        
        while True:
            user_input = input("\nAre you satisfied with this documentation? (yes/no): ").strip().lower()
            if user_input in ['yes', 'y']:
                return "", True
            elif user_input in ['no', 'n']:
                feedback = input("Please provide feedback to improve the documentation: ")
                return feedback, False
            else:
                print("Please answer 'yes' or 'no'.")
    
    def _handle_user_question(self, question: str) -> str:
        """
        Let the user answer a question instead of the VideoInterpreter.
        
        Args:
            question: The question to ask the user.
            
        Returns:
            The user's answer.
        """
        print("\n" + "="*50)
        print("QUESTION FROM DOC GENERATOR:")
        print("="*50)
        print(question)
        print("\n" + "="*50)
        
        user_answer = input("\nPlease answer this question (or type 'interpreter' to let the VideoInterpreter answer): ")
        
        if user_answer.strip().lower() == 'interpreter':
            print("Asking VideoInterpreter instead...")
            return self.video_interpreter.respond(question)
        
        return user_answer
    
    def generate_documentation(self) -> str:
        """
        Generate documentation based on the video transcription.
        
        This method orchestrates the workflow between DocGenerator and VideoInterpreter,
        handling questions, user feedback, and documentation refinement.
        
        Returns:
            The final documentation.
        """
        if not self.transcription:
            raise ValueError("No transcription available. Please load a video or transcription first.")
        
        print("Starting documentation generation workflow...")
        
        # First, get a detailed step-by-step description from the VideoInterpreter
        print("Getting initial step-by-step description from VideoInterpreter...")
        initial_description = self.video_interpreter.respond(
            "Please provide a detailed step-by-step description of what is happening in this video. "
            "Focus on the actions being performed, the sequence of steps, and any important visual details. "
            "Be as specific and comprehensive as possible."
        )
        print("Initial description received from VideoInterpreter.")
        
        # Set transcription and initial description in DocGenerator
        print("Preparing DocGenerator with transcription and initial description...")
        initial_prompt = f"""
        You will be creating a step-by-step guide based on a video.
        
        Here is the transcription of the video:
        
        TRANSCRIPTION:
        {self.transcription}
        
        Additionally, here is a detailed description of what happens in the video:
        
        VIDEO DESCRIPTION:
        {initial_description}
        
        Using both the transcription and the video description, create a comprehensive step-by-step guide.
        If you have any questions or need clarification about specific parts of the video, please ask.
        """
        
        # Initialize counters
        iteration_count = 0
        question_count = 0
        current_documentation = None
        is_satisfied = False
        
        # Start the documentation generation process
        response = self.doc_generator.generate_documentation_with_description(initial_prompt)
        structured_response = self._get_structured_response(response)
        
        while iteration_count < self.config.max_iterations and not is_satisfied:
            iteration_count += 1
            
            if structured_response.type == ResponseType.QUESTION:
                question_count += 1
                question = structured_response.content
                
                # Check if we should ask the user instead of the VideoInterpreter
                if question_count % self.config.user_feedback_interval == 0:
                    answer = self._handle_user_question(question)
                else:
                    print(f"\nQuestion from DocGenerator ({question_count}):")
                    print(question)
                    answer = self.video_interpreter.respond(question)
                    print(f"Answer from VideoInterpreter:")
                    print(answer)
                
                # Send the answer back to DocGenerator
                response = self.doc_generator.refine_documentation(f"ANSWER: {answer}")
                structured_response = self._get_structured_response(response)
            
            elif structured_response.type == ResponseType.DOCUMENTATION:
                current_documentation = structured_response.content
                
                # Check if we should get user feedback
                if iteration_count % self.config.user_feedback_interval == 0:
                    feedback, is_satisfied = self._get_user_feedback(current_documentation)
                    
                    if not is_satisfied and feedback:
                        # Refine documentation based on user feedback
                        response = self.doc_generator.refine_documentation(feedback)
                        structured_response = self._get_structured_response(response)
                    elif is_satisfied:
                        # User is satisfied, break the loop
                        break
                else:
                    # Continue with more iterations if needed
                    response = self.doc_generator.refine_documentation(
                        "Please review your documentation and identify any gaps or uncertainties. "
                        "If you have questions, ask them. If the documentation is complete, indicate so."
                    )
                    structured_response = self._get_structured_response(response)
            
            elif structured_response.type == ResponseType.COMPLETE:
                # DocGenerator indicates the documentation is complete
                current_documentation = structured_response.content
                feedback, is_satisfied = self._get_user_feedback(current_documentation)
                
                if not is_satisfied and feedback:
                    # Refine documentation based on user feedback
                    response = self.doc_generator.refine_documentation(feedback)
                    structured_response = self._get_structured_response(response)
                else:
                    # User is satisfied or provided no feedback
                    break
        
        # Save the final documentation
        if current_documentation:
            file_path = self.doc_generator.save_documentation()
            print(f"\nFinal documentation saved to: {file_path}")
            return current_documentation
        else:
            print("No documentation was generated.")
            return ""


# Example usage
if __name__ == "__main__":
    # Initialize VideoInstructor with a video file
    instructor = VideoInstructor(
        video_path="data/example_video.mp4",  # Place your video file in the data directory
        config=VideoInstructorConfig(
            user_feedback_interval=3,  # Get user feedback every 3 iterations
            max_iterations=15
        )
    )
    
    # Generate documentation
    documentation = instructor.generate_documentation()
    
    print("\nDocumentation generation complete!")
