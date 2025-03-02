#!/usr/bin/env python
"""
Example script demonstrating how to use the VideoInstruct package.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

from videoinstruct import VideoInstructor, VideoInstructorConfig
from videoinstruct.agents.DocGenerator import DocGeneratorConfig
from videoinstruct.agents.VideoInterpreter import VideoInterpreterConfig
from videoinstruct.agents.DocEvaluator import DocEvaluatorConfig

# Load environment variables from .env file
load_dotenv()

# Check if API keys are set
required_keys = ["OPENAI_API_KEY", "GEMINI_API_KEY", "DEEPSEEK_API_KEY"]
missing_keys = [key for key in required_keys if not os.getenv(key)]
if missing_keys:
    print(f"Error: Missing required API keys: {', '.join(missing_keys)}")
    print("Please set these keys in your .env file or environment variables.")
    exit(1)

# Create configuration
config = VideoInstructorConfig(
    doc_generator_config=DocGeneratorConfig(
        model="o3-mini",
        temperature=0.7,
        max_output_tokens=4000
    ),
    video_interpreter_config=VideoInterpreterConfig(
        model="gemini-2.0-flash",
        temperature=0.7
    ),
    doc_evaluator_config=DocEvaluatorConfig(
        model="deepseek/deepseek-reasoner",
        temperature=0.2,
        max_rejection_count=3
    ),
    user_feedback_interval=3,
    max_iterations=15,
    output_dir="output",
    temp_dir="temp"
)

def main():
    # Path to the video file
    video_path = Path("data/example_video.mp4")
    
    # Check if the video file exists
    if not video_path.exists():
        print(f"Error: Video file not found at {video_path}")
        print("Please place a video file at this location or update the path.")
        return
    
    # Initialize VideoInstructor
    print("Initializing VideoInstructor...")
    instructor = VideoInstructor(config)
    
    # Process the video
    print(f"Processing video: {video_path}")
    output_path = instructor.process_video(video_path)
    
    print(f"Documentation generated successfully: {output_path}")

if __name__ == "__main__":
    main() 