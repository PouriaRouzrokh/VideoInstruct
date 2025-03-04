import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the path so we can import the videoinstruct package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from videoinstruct.videoinstructor import VideoInstructor, VideoInstructorConfig
from videoinstruct.agents.DocGenerator import DocGeneratorConfig
from videoinstruct.agents.VideoInterpreter import VideoInterpreterConfig
from videoinstruct.agents.DocEvaluator import DocEvaluatorConfig

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Example usage of the VideoInstructor class.
    
    This script demonstrates how to use the VideoInstructor class to:
    1. Load a video file
    2. Extract its transcription
    3. Generate step-by-step documentation
    4. Evaluate documentation quality
    5. Handle questions and user feedback
    
    Before running this script:
    1. Place your video file in the 'data' directory
    2. Set the OPENAI_API_KEY, GEMINI_API_KEY, and DEEPSEEK_API_KEY environment variables in your .env file
    """
    # Get API keys from environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    
    if not openai_api_key or not gemini_api_key or not anthropic_api_key:
        print("Error: API keys not found. Please set OPENAI_API_KEY, GEMINI_API_KEY, and ANTHROPIC_API_KEY in your .env file.")
        return
    
    # Configure the VideoInstructor
    config = VideoInstructorConfig(
        # DocGenerator configuration
        doc_generator_config=DocGeneratorConfig(
            api_key=openai_api_key,
            model_provider="openai",
            model="o3-mini", 
            temperature=0.7,
            max_output_tokens=4000
        ),
        
        # VideoInterpreter configuration
        video_interpreter_config=VideoInterpreterConfig(
            api_key=gemini_api_key,
            model="gemini-2.0-flash",  # You can change this to any supported Gemini model
            temperature=0.7
        ),
        
        # DocEvaluator configuration
        doc_evaluator_config=DocEvaluatorConfig(
            api_key=deepseek_api_key,
            model_provider="deepseek",
            model="deepseek-reasoner", 
            temperature=0.2,
            max_rejection_count=3  # Number of rejections before escalating to user
        ),
        
        # VideoInstructor configuration
        max_iterations=15,
        output_dir="output",
        temp_dir="temp"
    )
    
    # Path to the video file - replace with your video file name
    video_file = "RG_Drive_Demonsration.mp4"  # Updated to match the actual file name
    video_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", video_file)
    
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        print("Please place your video file in the 'data' directory and update the video_file variable.")
        return
    
    # Initialize VideoInstructor
    instructor = VideoInstructor(
        video_path=video_path,
        config=config
    )
    
    # Generate documentation  
    documentation = instructor.generate_documentation()

if __name__ == "__main__":
    main() 