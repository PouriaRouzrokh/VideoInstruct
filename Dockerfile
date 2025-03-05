FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install VideoInstruct package directly from GitHub
RUN pip install git+https://github.com/PouriaRouzrokh/VideoInstruct.git

# Create necessary directories
RUN mkdir -p /app/data /app/output /app/temp

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Set default configuration values
ENV VIDEO_PATH=""
ENV ENV_FILE=""
ENV MAX_ITERATIONS=15
ENV OUTPUT_DIR="/app/output"
ENV TEMP_DIR="/app/temp"
ENV DOC_GENERATOR_MODEL="o3-mini"
ENV DOC_GENERATOR_TEMPERATURE=0.7
ENV DOC_GENERATOR_MAX_TOKENS=4000
ENV VIDEO_INTERPRETER_MODEL="gemini-2.0-flash"
ENV VIDEO_INTERPRETER_TEMPERATURE=0.7
ENV DOC_EVALUATOR_MODEL="deepseek-reasoner"
ENV DOC_EVALUATOR_TEMPERATURE=0.2
ENV DOC_EVALUATOR_MAX_REJECTIONS=3

# Create an entrypoint script
COPY <<EOF /app/docker-entrypoint.py
#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
from pathlib import Path
from dotenv import load_dotenv
from videoinstruct.videoinstructor import VideoInstructor, VideoInstructorConfig
from videoinstruct.agents.DocGenerator import DocGeneratorConfig
from videoinstruct.agents.VideoInterpreter import VideoInterpreterConfig
from videoinstruct.agents.DocEvaluator import DocEvaluatorConfig

def get_env_float(key, default):
    """Get float value from environment with default"""
    value = os.getenv(key, str(default))
    try:
        return float(value)
    except ValueError:
        print(f"Warning: Invalid value for {key}, using default: {default}")
        return default

def get_env_int(key, default):
    """Get integer value from environment with default"""
    value = os.getenv(key, str(default))
    try:
        return int(value)
    except ValueError:
        print(f"Warning: Invalid value for {key}, using default: {default}")
        return default

def download_video(url, target_dir="/app/data"):
    """Download video from URL using various supported methods"""
    try:
        import yt_dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(target_dir, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return os.path.join(target_dir, ydl.prepare_filename(info))
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='VideoInstruct Docker Entrypoint')
    parser.add_argument('--video', help='Path to the video file or URL')
    parser.add_argument('--env-file', help='Path to the .env file')
    args = parser.parse_args()
    
    # Load environment variables from file if specified
    env_file = args.env_file or os.getenv("ENV_FILE")
    if env_file and os.path.exists(env_file):
        load_dotenv(env_file)
    
    # Get API keys from environment
    openai_api_key = os.getenv("OPENAI_API_KEY")
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    
    if not all([openai_api_key, gemini_api_key, deepseek_api_key]):
        print("Error: Missing required API keys. Please set all required environment variables.")
        sys.exit(1)
    
    # Handle video path or URL
    video_path = args.video or os.getenv("VIDEO_PATH")
    if video_path:
        if video_path.startswith(('http://', 'https://', 'www.')):
            print(f"Downloading video from URL: {video_path}")
            video_path = download_video(video_path)
            if not video_path:
                sys.exit(1)
        elif not os.path.exists(video_path):
            print(f"Error: Video file not found at {video_path}")
            sys.exit(1)
    else:
        # Find first video in data directory
        video_files = [f for f in os.listdir("/app/data") if f.endswith((".mp4", ".avi", ".mov"))]
        if not video_files:
            print("Error: No video files found in data directory and no video path/URL provided.")
            sys.exit(1)
        video_path = os.path.join("/app/data", video_files[0])
    
    print(f"Processing video: {video_path}")
    
    # Configure VideoInstructor with environment variables
    config = VideoInstructorConfig(
        doc_generator_config=DocGeneratorConfig(
            api_key=openai_api_key,
            model_provider="openai",
            model=os.getenv("DOC_GENERATOR_MODEL", "o3-mini"),
            temperature=get_env_float("DOC_GENERATOR_TEMPERATURE", 0.7),
            max_output_tokens=get_env_int("DOC_GENERATOR_MAX_TOKENS", 4000)
        ),
        video_interpreter_config=VideoInterpreterConfig(
            api_key=gemini_api_key,
            model=os.getenv("VIDEO_INTERPRETER_MODEL", "gemini-2.0-flash"),
            temperature=get_env_float("VIDEO_INTERPRETER_TEMPERATURE", 0.7)
        ),
        doc_evaluator_config=DocEvaluatorConfig(
            api_key=deepseek_api_key,
            model_provider="deepseek",
            model=os.getenv("DOC_EVALUATOR_MODEL", "deepseek-reasoner"),
            temperature=get_env_float("DOC_EVALUATOR_TEMPERATURE", 0.2),
            max_rejection_count=get_env_int("DOC_EVALUATOR_MAX_REJECTIONS", 3)
        ),
        max_iterations=get_env_int("MAX_ITERATIONS", 15),
        output_dir=os.getenv("OUTPUT_DIR", "/app/output"),
        temp_dir=os.getenv("TEMP_DIR", "/app/temp")
    )
    
    # Initialize and run VideoInstructor
    instructor = VideoInstructor(
        video_path=video_path,
        config=config
    )
    
    documentation = instructor.generate_documentation()
    print("\nDocumentation generation completed!")
    print("Results are available in the output directory.")

if __name__ == "__main__":
    main()
EOF

RUN chmod +x /app/docker-entrypoint.py

# Install additional dependencies for video download support
RUN pip install yt-dlp

# Set the default command to run our entrypoint script
ENTRYPOINT ["python", "/app/docker-entrypoint.py"]
CMD [] 