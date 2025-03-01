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

## Project Structure

```
VideoInstruct/
├── data/                  # Place your video files here
├── examples/              # Example usage scripts
├── output/                # Generated documentation output
├── temp/                  # Temporary files (transcriptions, etc.)
├── videoinstruct/         # Main package
│   ├── agents/            # AI agent modules
│   │   ├── DocGenerator.py    # Documentation generation agent
│   │   ├── DocEvaluator.py    # Documentation evaluation agent
│   │   └── VideoInterpreter.py # Video interpretation agent
│   ├── utils/             # Utility functions
│   │   └── transcription.py   # Video transcription utilities
│   └── videoinstructor.py # Main orchestration class
└── README.md              # This file
```

## Requirements

- Python 3.8+
- OpenAI API key (for DocGenerator)
- Google Gemini API key (for VideoInterpreter)
- DeepSeek API key (for DocEvaluator)
- FFmpeg (for video processing)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/VideoInstruct.git
   cd VideoInstruct
   ```

2. Create a virtual environment and install dependencies:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GEMINI_API_KEY=your_gemini_api_key
   DEEPSEEK_API_KEY=your_deepseek_api_key
   ```

## Usage

1. Place your video file in the `data` directory.

2. Run the example script:

   ```
   python examples/example_usage.py
   ```

3. The script will:
   - Extract the transcription from your video
   - Get a detailed description from the VideoInterpreter
   - Generate step-by-step documentation using the DocGenerator
   - Ask questions to the VideoInterpreter when needed
   - Evaluate documentation quality using the DocEvaluator
   - Escalate to human user after a configurable number of rejections
   - Collect your feedback to refine the documentation
   - Save the final documentation to the `output` directory

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
8. **Output**: Final documentation is saved as markdown

## Customization

You can customize the behavior of VideoInstruct by modifying the configuration parameters:

```python
config = VideoInstructorConfig(
    # DocGenerator configuration
    doc_generator_config=DocGeneratorConfig(
        model="gpt-4o-mini",  # Change to any supported model
        temperature=0.7,
        max_output_tokens=4000
    ),

    # VideoInterpreter configuration
    video_interpreter_config=VideoInterpreterConfig(
        model="gemini-2.0-flash",  # Change to any supported Gemini model
        temperature=0.7
    ),

    # DocEvaluator configuration
    doc_evaluator_config=DocEvaluatorConfig(
        model="deepseek/deepseek-reasoner",  # Change to any supported model
        temperature=0.2,
        max_rejection_count=3  # Number of rejections before escalating to user
    ),

    # VideoInstructor configuration
    user_feedback_interval=3,  # Get user feedback every 3 iterations
    max_iterations=15,
    output_dir="output",
    temp_dir="temp"
)
```

## License

[MIT License](LICENSE)
