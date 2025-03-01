import os
import time
import datetime
from typing import List, Optional, Dict, Any, Union, Tuple
import json
import re
import base64
from markdown_pdf import MarkdownPdf, Section

from videoinstruct.agents.VideoInterpreter import VideoInterpreter
from videoinstruct.agents.DocGenerator import DocGenerator
from videoinstruct.agents.DocEvaluator import DocEvaluator
from videoinstruct.utils.transcription import transcribe_video
from videoinstruct.configs import (
    VideoInterpreterConfig, 
    DocGeneratorConfig, 
    DocEvaluatorConfig,
    ResponseType,
    DocGeneratorResponse,
    VideoInstructorConfig
)


class VideoInstructor:
    """
    A class that orchestrates the workflow between DocGenerator, VideoInterpreter, and DocEvaluator.
    
    This class handles:
    1. Video transcription extraction
    2. Passing transcription to DocGenerator
    3. Managing the Q&A flow between DocGenerator and VideoInterpreter
    4. Evaluating documentation quality with DocEvaluator
    5. Collecting user feedback and refining documentation
    """
    
    def __init__(
        self,
        video_path: Optional[str] = None,
        transcription_path: Optional[str] = None,
        config: Optional[VideoInstructorConfig] = None
    ):
        """
        Initialize the VideoInstructor.
        
        Args:
            video_path: Path to the video file.
            transcription_path: Path to an existing transcription file (optional).
            config: Configuration for the VideoInstructor, including API keys and model settings.
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
        
        # Create a timestamped directory for this session
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_dir = os.path.join(self.config.output_dir, self.timestamp)
        os.makedirs(self.session_dir, exist_ok=True)
        
        # Initialize DocGenerator with configuration
        self.doc_generator = DocGenerator(
            config=self.config.doc_generator_config,
            output_dir=self.session_dir
        )
        
        # Initialize VideoInterpreter with configuration
        self.video_interpreter = VideoInterpreter(
            config=self.config.video_interpreter_config
        )
        
        # Initialize DocEvaluator with configuration
        self.doc_evaluator = DocEvaluator(
            config=self.config.doc_evaluator_config
        )
        
        # Track document versions
        self.doc_version = 0
        
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
                # If the response has a type field, ensure it's one of our valid types
                if json_response["type"] not in [ResponseType.DOCUMENTATION, ResponseType.QUESTION]:
                    json_response["type"] = ResponseType.DOCUMENTATION
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
    
    def _save_documentation(self, documentation: str, is_final: bool = False) -> str:
        """
        Save the documentation to a file with version tracking.
        
        Args:
            documentation: The documentation content to save.
            is_final: Whether this is the final approved version.
            
        Returns:
            The path to the saved file.
        """
        if not documentation:
            return ""
        
        base_filename = "documentation"
        
        # Add version number and final suffix if applicable
        if is_final:
            filename = f"{base_filename}_final.md"
        else:
            self.doc_version += 1
            filename = f"{base_filename}_v{self.doc_version}.md"
        
        # Full path to save the file
        file_path = os.path.join(self.session_dir, filename)
        
        # Save documentation to file
        with open(file_path, 'w') as f:
            f.write(documentation)
        
        print(f"Documentation saved to {file_path}")
        
        # Generate PDF version of the documentation
        pdf_path = os.path.splitext(file_path)[0] + ".pdf"
        try:
            # Create a MarkdownPdf instance
            pdf = MarkdownPdf()
            
            # Add the documentation as a section
            pdf.add_section(Section(documentation))
            
            # Set metadata
            pdf.meta["title"] = os.path.basename(pdf_path)
            pdf.meta["author"] = "VideoInstructor"
            
            # Save the PDF
            pdf.save(pdf_path)
            print(f"PDF version saved to {pdf_path}")
        except Exception as e:
            print(f"Error generating PDF: {str(e)}")
        
        return file_path
    
    def _evaluate_documentation(self, documentation: str, print_documentation: bool = True) -> Tuple[bool, str]:
        """
        Evaluate the documentation using the DocEvaluator.
        
        Args:
            documentation: The documentation to evaluate.
            print_documentation: Whether to print the documentation to the console.
            
        Returns:
            A tuple of (is_approved, feedback)
        """
        # Show the documentation to the user before evaluation if requested
        if print_documentation:
            print("\n" + "="*50)
            print("GENERATED DOCUMENTATION:")
            print("="*50)
            print(documentation)
            print("\n" + "="*50)
        
        print("EVALUATING DOCUMENTATION...")
        
        # Find the PDF file path based on the current version
        pdf_path = os.path.join(self.session_dir, f"documentation_v{self.doc_version}.pdf")
        
        # Check if PDF exists
        if os.path.exists(pdf_path):
            try:
                # Read the PDF file
                with open(pdf_path, 'rb') as file:
                    pdf_data = file.read()
                
                # Encode the PDF as base64
                encoded_pdf = base64.b64encode(pdf_data).decode("utf-8")
                base64_url = f"data:application/pdf;base64,{encoded_pdf}"
                
                # Create content with both text and PDF
                content = [
                    {"type": "text", "text": f"""
                    Please evaluate the following documentation for quality, clarity, and completeness.
                    The documentation is provided as PDF.
                    """},
                    {"type": "image_url", "image_url": base64_url}
                ]
                
                # Evaluate with PDF
                is_approved, feedback = self.doc_evaluator.evaluate_documentation_with_pdf(content)
            except Exception as e:
                print(f"Error processing PDF for evaluation: {str(e)}")
                # Fall back to text-only evaluation
                is_approved, feedback = self.doc_evaluator.evaluate_documentation(documentation)
        else:
            # Fall back to text-only evaluation
            is_approved, feedback = self.doc_evaluator.evaluate_documentation(documentation)
        
        if is_approved:
            print("Documentation APPROVED by DocEvaluator")
            print(f"Feedback: {feedback}")
        else:
            print("Documentation REJECTED by DocEvaluator")
            print(f"Feedback: {feedback}")
            
            # Print the number of rejections so far
            print(f"Rejection count: {self.doc_evaluator.rejection_count}/{self.doc_evaluator.config.max_rejection_count}")
            
            if self.doc_evaluator.should_escalate_to_user():
                print("Maximum rejections reached. Will escalate to user.")
        
        return is_approved, feedback
    
    def _get_user_feedback(self, documentation: str) -> Tuple[str, bool]:
        """
        Get feedback from the user about the documentation.
        
        Args:
            documentation: The documentation to get feedback on.
            
        Returns:
            A tuple of (feedback, is_satisfied)
        """
        # Show the most recent feedback if available
        most_recent_feedback = ""
        if self.doc_evaluator.feedback_history and len(self.doc_evaluator.feedback_history) > 0:
            most_recent_feedback = self.doc_evaluator.feedback_history[-1]
            print("\nMost recent evaluator feedback:")
            print(most_recent_feedback)
        
        # Check if PDF exists and inform the user
        pdf_path = os.path.join(self.session_dir, f"documentation_v{self.doc_version}.pdf")
        if os.path.exists(pdf_path):
            print(f"\nA PDF version of the documentation is available at: {pdf_path}")
        
        while True:
            user_input = input("\nAre you satisfied with this documentation? (yes/no): ").strip().lower()
            if user_input in ['yes', 'y']:
                # Save the final version with _final suffix (this will also generate the PDF)
                md_path = self._save_documentation(documentation, is_final=True)
                return "", True
            elif user_input in ['no', 'n']:
                feedback = input("Please provide feedback to improve the documentation (press Enter to use evaluator's feedback): ")
                # If user just presses Enter, use the most recent feedback from the evaluator
                if not feedback.strip() and most_recent_feedback:
                    print(f"Using evaluator's feedback: {most_recent_feedback}")
                    return most_recent_feedback, False
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
    
    def _prepare_initial_prompt(self) -> str:
        """
        Prepare the initial prompt for documentation generation by combining
        the transcription and a detailed description from the VideoInterpreter.
        
        Returns:
            A formatted initial prompt string for the DocGenerator.
        """
        # First, get a detailed step-by-step description from the VideoInterpreter
        print("Getting initial step-by-step description from VideoInterpreter...")
        initial_description = self.video_interpreter.respond(
            "Please provide a detailed step-by-step description of what is happening in this video. "
            "Focus on the actions being performed, the sequence of steps, and any important visual details. "
            "Be as specific and comprehensive as possible."
        )
        print("Initial description received from VideoInterpreter.")
        
        # Prepare the initial prompt with transcription and description
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
        
        return initial_prompt
    
    def generate_documentation(self) -> str:
        """
        Generate step-by-step documentation from the loaded video.
        
        Returns:
            The generated documentation as a string.
        """
        if not self.transcription:
            raise ValueError("No transcription available. Please load a video or transcription first.")
        
        print("Starting documentation generation workflow...")
        
        # Reset DocEvaluator memory at the start of a new documentation generation
        self.doc_evaluator.reset_memory()
        
        # Reset document version counter
        self.doc_version = 0
        
        # Prepare the initial prompt
        initial_prompt = self._prepare_initial_prompt()
        
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
                
                # Save the current version of the documentation
                self._save_documentation(current_documentation)
                
                # Print the documentation when it's first generated or refined
                print("\n" + "="*50)
                print("GENERATED DOCUMENTATION:")
                print("="*50)
                print(current_documentation)
                print("\n" + "="*50)
                
                # First, let the DocEvaluator evaluate the documentation
                evaluation_count = self.doc_evaluator.rejection_count + 1
                print(f"\nEvaluation round #{evaluation_count}")
                
                # Don't print the documentation during evaluation since we just printed it
                is_approved, feedback = self._evaluate_documentation(current_documentation, print_documentation=False)
                
                print(f"Evaluator's feedback: {feedback}")

                # Check if we should escalate to user due to repeated rejections
                if not is_approved and self.doc_evaluator.should_escalate_to_user():
                    print("\n" + "="*50)
                    print("ESCALATING TO USER: DocEvaluator has rejected the documentation multiple times.")
                    print("="*50)
                    user_feedback, is_satisfied = self._get_user_feedback(current_documentation)
                    
                    # Reset the rejection count after user intervention
                    self.doc_evaluator.reset_rejection_count()
                    
                    if not is_satisfied and user_feedback:
                        # Refine documentation based on user feedback
                        response = self.doc_generator.refine_documentation(user_feedback)
                        structured_response = self._get_structured_response(response)
                    elif is_satisfied:
                        # User is satisfied, break the loop
                        break
                
                # If DocEvaluator approved or we're continuing after rejection
                elif is_approved:
                    # DocEvaluator approved, now get user feedback
                    user_feedback, is_satisfied = self._get_user_feedback(current_documentation)
                    
                    if not is_satisfied and user_feedback:
                        # Refine documentation based on user feedback
                        response = self.doc_generator.refine_documentation(user_feedback)
                        structured_response = self._get_structured_response(response)
                    elif is_satisfied:
                        # User is satisfied, break the loop
                        break
                else:
                    # DocEvaluator rejected but not enough times to escalate to user
                    # Refine documentation based on DocEvaluator feedback
                    response = self.doc_generator.refine_documentation(f"FEEDBACK: {feedback}")
                    structured_response = self._get_structured_response(response)
                
                # Check if we should get user feedback based on iteration count
                if not is_approved and iteration_count % self.config.user_feedback_interval == 0:
                    user_feedback, is_satisfied = self._get_user_feedback(current_documentation)
                    
                    if not is_satisfied and user_feedback:
                        # Refine documentation based on user feedback
                        response = self.doc_generator.refine_documentation(user_feedback)
                        structured_response = self._get_structured_response(response)
                    elif is_satisfied:
                        # User is satisfied, break the loop
                        break
        
        # Return the final documentation
        if current_documentation:
            print(f"\nFinal documentation saved in: {self.session_dir}")
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
            # Set API keys in the configs
            doc_generator_config=DocGeneratorConfig(
                api_key=os.getenv("OPENAI_API_KEY"),
                model_provider="openai",
                model="gpt-4o"
            ),
            video_interpreter_config=VideoInterpreterConfig(
                api_key=os.getenv("GEMINI_API_KEY"),
                model="gemini-2.0-flash"
            ),
            doc_evaluator_config=DocEvaluatorConfig(
                api_key=os.getenv("DEEPSEEK_API_KEY"),
                model_provider="deepseek",
                model="deepseek-reasoner"
            ),
            user_feedback_interval=3,  # Get user feedback every 3 iterations
            max_iterations=15
        )
    )
    
    # Generate documentation
    documentation = instructor.generate_documentation()
    
    print("\nDocumentation generation complete!")
