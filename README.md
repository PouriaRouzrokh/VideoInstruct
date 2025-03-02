# VideoInstruct

VideoInstruct is a tool that automatically generates step-by-step documentation from instructional videos. It uses AI to extract transcriptions, interpret video content, and create comprehensive markdown guides.

## Features

- Automatic video transcription extraction
- AI-powered video interpretation
- Step-by-step documentation generation
- Automated documentation quality evaluation with conversation memory
- Interactive Q&A workflow between AI agents
- User feedback integration for documentation refinement
- Configurable escalation to human users
- Screenshot generation and annotation
- PDF export capabilities

## Project Structure

```
VideoInstruct/
├── data/                  # Place your video files here
├── examples/              # Example usage scripts
│   ├── example_usage.py   # Basic example with repository structure
├── output/                # Generated documentation output
├── videoinstruct/         # Main package
│   ├── agents/            # AI agent modules
│   │   ├── DocGenerator.py      # Documentation generation agent
│   │   ├── DocEvaluator.py      # Documentation evaluation agent
│   │   ├── VideoInterpreter.py  # Video interpretation agent
│   │   └── ScreenshotAgent.py   # Screenshot generation agent
│   ├── prompts/           # System prompts for agents
│   ├── tools/             # Utility tools
│   │   ├── image_annotator.py   # Image annotation tools
│   │   └── video_screenshot.py  # Video screenshot tools
│   ├── utils/             # Utility functions
│   │   ├── transcription.py     # Video transcription utilities
│   │   └── md2pdf.py            # Markdown to PDF conversion
│   ├── cli.py             # Command-line interface
│   ├── configs.py         # Configuration classes
│   ├── prompt_loader.py   # Prompt loading utilities
│   └── videoinstructor.py # Main orchestration class
├── .env                   # Environment variables (API keys)
├── MANIFEST.in            # Package manifest file
├── pyproject.toml         # Python project configuration
├── requirements.txt       # Package dependencies
├── setup.py               # Package setup file
└── README.md              # This file
```

## Requirements

- Python 3.8+
- OpenAI API key (for DocGenerator)
- Google Gemini API key (for VideoInterpreter)
- DeepSeek API key (for DocEvaluator)
- FFmpeg (for video processing)

## Installation

### From PyPI

```bash
pip install videoinstruct
```

### From Source

1. Clone the repository:

   ```bash
   git clone https://github.com/PouriaRouzrokh/VideoInstruct.git
   cd VideoInstruct
   ```

2. Install the package in development mode:

   ```bash
   pip install -e .
   ```

3. Create a `.env` file in the root directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GEMINI_API_KEY=your_gemini_api_key
   DEEPSEEK_API_KEY=your_deepseek_api_key
   ```

## Examples

The repository includes two example scripts to help you get started:

1. **example_usage.py**: Demonstrates direct usage with the repository structure and hardcoded paths. This is useful if you're working directly with the repository without installing it as a package.

2. **package_usage.py**: Shows how to use VideoInstruct after it's been installed as a package. This example demonstrates:
   - Using VideoInstruct as an imported Python package in your code
   - Using VideoInstruct from the command line

To run the examples:

```bash
# Run the basic example
python examples/example_usage.py

# Run the package usage example
python examples/package_usage.py
```

## Using as a Python Package

You can use VideoInstruct as a Python package in your own projects:

```python
from videoinstruct import VideoInstructor, VideoInstructorConfig
from videoinstruct.agents.DocGenerator import DocGeneratorConfig
from videoinstruct.agents.VideoInterpreter import VideoInterpreterConfig
from videoinstruct.agents.DocEvaluator import DocEvaluatorConfig
from pathlib import Path

# Create configuration
config = VideoInstructorConfig(
    doc_generator_config=DocGeneratorConfig(
        model="gpt-4o-mini",
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

# Initialize VideoInstructor
instructor = VideoInstructor(config)

# Process a video
video_path = Path("path/to/your/video.mp4")
output_path = instructor.process_video(video_path)

print(f"Documentation generated successfully: {output_path}")
```

## Using the Command Line Interface

VideoInstruct comes with a command-line interface:

```bash
# Basic usage
videoinstruct path/to/your/video.mp4

# With custom options
videoinstruct path/to/your/video.mp4 \
    --output-dir custom_output \
    --temp-dir custom_temp \
    --max-iterations 10 \
    --user-feedback-interval 2 \
    --doc-generator-model "gpt-4o" \
    --video-interpreter-model "gemini-2.0-pro" \
    --doc-evaluator-model "deepseek/deepseek-reasoner"
```

## Workflow

VideoInstruct follows this workflow:

1. **Transcription**: Extract text from the video
2. **Initial Description**: Get a detailed visual description from VideoInterpreter
3. **Documentation Generation**: DocGenerator creates initial documentation
4. **User Preview**: Generated documentation is shown to the user before evaluation
5. **Documentation Evaluation**: DocEvaluator assesses documentation quality
   - Provides feedback on each evaluation round
   - Maintains conversation memory for context-aware evaluation
   - Escalates to human user after a configurable number of rejections
6. **Refinement**: Documentation is refined based on evaluator feedback
7. **User Feedback**: User provides final approval or additional feedback
8. **Output**: Final documentation is saved as markdown and optionally as PDF

## Development

To contribute to VideoInstruct:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

[MIT License](LICENSE)
