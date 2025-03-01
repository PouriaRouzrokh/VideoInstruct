# VideoInstruct

VideoInstruct is a tool that automatically generates step-by-step documentation from instructional videos. It uses AI to extract transcriptions, interpret video content, and create comprehensive markdown guides.

## Features

- Automatic video transcription extraction
- AI-powered video interpretation
- Step-by-step documentation generation
- Interactive Q&A workflow between AI agents
- User feedback integration for documentation refinement

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
   - Collect your feedback to refine the documentation
   - Save the final documentation to the `output` directory

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

    # VideoInstructor configuration
    user_feedback_interval=3,  # Get user feedback every 3 iterations
    max_iterations=15,
    output_dir="output",
    temp_dir="temp"
)
```

## License

[MIT License](LICENSE)
