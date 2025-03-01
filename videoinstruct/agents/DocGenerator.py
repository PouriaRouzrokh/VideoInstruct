import os
import time
from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
import json
import litellm
from IPython.display import Markdown
import markdown
import re

# System prompt for DocGenerator
# This is defined outside the class for easy editing
DOC_GENERATOR_SYSTEM_PROMPT = """
You are an expert technical writer who creates clear, concise step-by-step guides based on video transcriptions.
Your task is to generate a detailed markdown guide that explains how to perform the task demonstrated in the video.

Follow these guidelines:
1. Create a clear title that describes the task
2. Write an introduction explaining what the task accomplishes
3. Break down the task into numbered steps with clear instructions
4. Use markdown formatting for clarity (headers, lists, code blocks, etc.)
5. If you're uncertain about any details in the transcription, formulate specific questions to ask
6. Focus on being precise and actionable - users should be able to follow your guide without watching the video

When you need to ask a question, respond with a JSON object in this format:
{
  "type": "question",
  "content": "Your specific question here"
}

When you're providing documentation, respond with a JSON object in this format:
{
  "type": "documentation",
  "content": "Your markdown documentation here"
}

When you believe the documentation is complete and no further questions are needed, respond with:
{
  "type": "complete",
  "content": "Your final markdown documentation here"
}

Remember that you only have access to the video transcription, not the video itself. If you need visual details,
you must ask specific questions to get that information.
"""

class DocGeneratorConfig(BaseModel):
    """Configuration for the DocGenerator class."""
    model: str = Field(default="gpt-4o-mini")
    system_instruction: str = Field(default=DOC_GENERATOR_SYSTEM_PROMPT)
    max_output_tokens: Optional[int] = None
    temperature: float = Field(default=0.7)
    top_p: Optional[float] = None
    stream: bool = Field(default=False)
    seed: Optional[int] = None
    response_format: Optional[Dict[str, Any]] = Field(default={"type": "json_object"})


class DocGenerator:
    """
    A class for generating step-by-step documentation based on video transcriptions.
    Works with LiteLLM to support various LLM providers.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_provider: str = "openai",
        transcription: Optional[str] = None,
        config: Optional[DocGeneratorConfig] = None,
        output_dir: str = "output"
    ):
        """
        Initialize the DocGenerator.
        
        Args:
            api_key: The API key for the LLM provider. If None, it will try to read from environment variables.
            model_provider: The LLM provider (e.g., "openai", "anthropic", "ollama").
            transcription: The transcription of the video to generate documentation for.
            config: Configuration for the LLM model.
            output_dir: Directory to save the generated documentation.
        """
        self.model_provider = model_provider
        self.transcription = transcription
        self.config = config or DocGeneratorConfig()
        self.conversation_history = []
        self.output_dir = output_dir
        
        # Set API key based on provider
        if api_key:
            if model_provider == "openai":
                os.environ["OPENAI_API_KEY"] = api_key
            elif model_provider == "anthropic":
                os.environ["ANTHROPIC_API_KEY"] = api_key
            # Add other providers as needed
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def set_transcription(self, transcription: str) -> None:
        """
        Set the video transcription.
        
        Args:
            transcription: The transcription of the video.
        """
        self.transcription = transcription
        # Reset conversation history when setting a new transcription
        self.conversation_history = []
    
    def generate_documentation(self) -> str:
        """
        Generate step-by-step documentation based on the video transcription.
        
        Returns:
            The generated documentation in markdown format or a structured JSON response.
        """
        if not self.transcription:
            raise ValueError("No transcription provided. Please set a transcription first.")
        
        # Initial prompt to generate documentation
        initial_prompt = f"""
        Based on the following video transcription, create a step-by-step guide:
        
        TRANSCRIPTION:
        {self.transcription}
        
        Generate a detailed markdown guide that explains how to perform the task shown in the video.
        If you have any questions or need clarification about specific parts of the video, please ask.
        """
        
        # Add initial prompt to conversation history
        self.conversation_history.append({"role": "user", "content": initial_prompt})
        
        # Generate response
        response = self._get_llm_response(self.conversation_history)
        
        # Add assistant response to conversation history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def generate_documentation_with_description(self, initial_prompt: str) -> str:
        """
        Generate step-by-step documentation based on both video transcription and a detailed description.
        
        Args:
            initial_prompt: A prompt containing both the transcription and a detailed description
                           of the video from the VideoInterpreter.
                           
        Returns:
            The generated documentation in markdown format or a structured JSON response.
        """
        # Add initial prompt to conversation history
        self.conversation_history.append({"role": "user", "content": initial_prompt})
        
        # Generate response
        response = self._get_llm_response(self.conversation_history)
        
        # Add assistant response to conversation history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def refine_documentation(self, feedback: str) -> str:
        """
        Refine the documentation based on feedback or additional information.
        
        Args:
            feedback: Feedback or additional information to improve the documentation.
            
        Returns:
            The refined documentation in markdown format or a structured JSON response.
        """
        if not self.conversation_history:
            raise ValueError("No documentation has been generated yet.")
        
        # Add feedback to conversation history
        self.conversation_history.append({"role": "user", "content": feedback})
        
        # Generate response
        response = self._get_llm_response(self.conversation_history)
        
        # Add assistant response to conversation history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def _get_llm_response(self, messages: List[Dict[str, str]]) -> str:
        """
        Get a response from the LLM.
        
        Args:
            messages: The conversation history.
            
        Returns:
            The LLM's response as text.
        """
        # Prepare model name based on provider
        model_name = self.config.model
        if self.model_provider != "openai" and not "/" in model_name:
            model_name = f"{self.model_provider}/{model_name}"
        
        # Prepare configuration for the API call
        generate_config = {}
        if self.config.max_output_tokens:
            generate_config["max_tokens"] = self.config.max_output_tokens
        if self.config.temperature:
            generate_config["temperature"] = self.config.temperature
        if self.config.top_p:
            generate_config["top_p"] = self.config.top_p
        if self.config.stream:
            generate_config["stream"] = self.config.stream
        if self.config.seed:
            generate_config["seed"] = self.config.seed
        if self.config.response_format:
            generate_config["response_format"] = self.config.response_format
        
        # Ensure drop_params is set to true
        generate_config["drop_params"] = True

        # Add system instruction if provided
        if self.config.system_instruction:
            system_message = {"role": "system", "content": self.config.system_instruction}
            messages = [system_message] + messages
        
        try:
            # Generate response using litellm
            response = litellm.completion(
                model=model_name,
                messages=messages,
                **generate_config
            )
            
            # Extract text from response
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return f"Error: {str(e)}"
    
    def save_documentation(self, filename: str = None) -> str:
        """
        Save the generated documentation to a markdown file.
        
        Args:
            filename: The name of the file to save the documentation to.
                     If None, a default name will be generated.
                     
        Returns:
            The path to the saved file.
        """
        if not self.conversation_history:
            raise ValueError("No documentation has been generated yet.")
        
        # Get the latest documentation
        latest_doc = None
        for message in reversed(self.conversation_history):
            if message["role"] == "assistant":
                content = message["content"]
                # Try to parse as JSON
                try:
                    json_content = json.loads(content)
                    if isinstance(json_content, dict) and "content" in json_content:
                        if json_content.get("type") in ["documentation", "complete"]:
                            latest_doc = json_content["content"]
                            break
                except json.JSONDecodeError:
                    # If not JSON, check if it's not a question
                    if not content.strip().endswith("?") and not content.startswith("VIDEO RESPONSE:"):
                        latest_doc = content
                        break
        
        if not latest_doc:
            raise ValueError("No documentation found in conversation history.")
        
        # Generate filename if not provided
        if not filename:
            # Extract title from markdown
            title_match = re.search(r'^#\s+(.+)$', latest_doc, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
                # Convert title to filename-friendly format
                filename = re.sub(r'[^\w\s-]', '', title).strip().lower()
                filename = re.sub(r'[-\s]+', '-', filename)
            else:
                # Use timestamp if no title found
                filename = f"documentation-{int(time.time())}"
        
        # Ensure filename has .md extension
        if not filename.endswith('.md'):
            filename += '.md'
        
        # Full path to save the file
        file_path = os.path.join(self.output_dir, filename)
        
        # Save documentation to file
        with open(file_path, 'w') as f:
            f.write(latest_doc)
        
        print(f"Documentation saved to {file_path}")
        return file_path
    
    def display_documentation(self) -> None:
        """
        Display the latest documentation as Markdown (useful in Jupyter notebooks).
        """
        if not self.conversation_history:
            raise ValueError("No documentation has been generated yet.")
        
        # Get the latest documentation
        latest_doc = None
        for message in reversed(self.conversation_history):
            if message["role"] == "assistant":
                content = message["content"]
                # Try to parse as JSON
                try:
                    json_content = json.loads(content)
                    if isinstance(json_content, dict) and "content" in json_content:
                        if json_content.get("type") in ["documentation", "complete"]:
                            latest_doc = json_content["content"]
                            break
                except json.JSONDecodeError:
                    # If not JSON, check if it's not a question
                    if not content.strip().endswith("?") and not content.startswith("VIDEO RESPONSE:"):
                        latest_doc = content
                        break
        
        if not latest_doc:
            raise ValueError("No documentation found in conversation history.")
        
        return Markdown(latest_doc)
    
    def _extract_questions(self, text: str) -> List[str]:
        """
        Extract questions from text.
        
        Args:
            text: Text containing questions.
            
        Returns:
            List of extracted questions.
        """
        # Simple pattern matching for questions
        questions = re.findall(r'(?:^|\n)\s*\d+\.\s*([^\n]+\?)', text)
        
        # If numbered list not found, try to find sentences ending with question marks
        if not questions:
            questions = re.findall(r'([^.!?\n]+\?)', text)
        
        return questions


# Example usage:
# doc_generator = DocGenerator(model_provider="openai")
# doc_generator.set_transcription("This is a transcription of a video showing how to create a new GitHub repository...")
# documentation = doc_generator.generate_documentation()
# print(documentation)
