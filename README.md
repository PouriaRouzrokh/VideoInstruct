# Multiagent VideoInstruct Framework

## Project Overview

This project develops a multiagent framework that transforms video demonstrations into comprehensive PDF documentation with text and annotated images. The system uses specialized agents working collaboratively to interpret video content, generate clear documentation, and ensure quality through evaluation and feedback.

## Workflow

1. User provides a video demonstration of a task
2. The system processes the video and generates detailed step-by-step documentation
3. The documentation undergoes evaluation and revision until quality standards are met
4. A final PDF with text and annotated images is delivered to the user

## Agents

### 1. DocGenerator

**Primary Role**: Create detailed PDF documentation with text and annotated images based on video demonstrations.

**Inputs**:

- Timed transcript of the video (with timestamps)
- Feedback from DocEvaluator (when available)

**Output**:

- PDF documentation with step-by-step instructions and annotated images

**Access to**:

- VideoInterpretor agent for answering questions about video content
- Screenshot tool to capture specific video frames
- ImageAnnotator agent for creating annotated images
- Previous feedback from DocEvaluator (when available)

### 2. VideoInterpretor

**Primary Role**: Analyze and interpret video content to answer the DocGenerator's questions.

**Inputs**:

- Video file
- Specific questions from DocGenerator

**Output**:

- Detailed answers about video content

### 3. ImageAnnotator

**Primary Role**: Create annotated images from video screenshots based on DocGenerator's requirements.

**Inputs**:

- Screenshot from video
- Annotation instructions from DocGenerator

**Output**:

- Annotated image with bounding boxes, arrows, and labels

**Tools**:

- ImageAnnotatorTool: Creates annotations based on element locations and connections
- ImageElementDetector: Automatically identifies and locates elements in the image

### 4. DocEvaluator

**Primary Role**: Review documentation for clarity and completeness, providing feedback for improvement.

**Inputs**:

- PDF documentation from DocGenerator

**Output**:

- Detailed feedback and improvement suggestions

## Termination Conditions

The documentation generation process continues until either:

1. A predetermined maximum number of revision rounds is reached, or
2. DocEvaluator confirms the documentation meets all quality standards with no further changes needed

## Process Flow

1. DocGenerator analyzes the timed transcript
2. DocGenerator consults VideoInterpretor as needed for clarification
3. DocGenerator captures screenshots at key moments
4. DocGenerator requests ImageAnnotator to enhance screenshots with visual guides
5. DocGenerator creates the initial PDF documentation
6. DocEvaluator reviews the documentation and provides feedback
7. Steps 1-6 repeat until termination conditions are met
8. Final PDF documentation is delivered
