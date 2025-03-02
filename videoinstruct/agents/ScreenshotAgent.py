import os
import re
import base64
import sys
from typing import Optional
from PIL import Image
from google import generativeai as genai
from io import BytesIO
import cv2
import ast
import shutil

# Add the parent directory to the Python path so we can import our modules
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from videoinstruct.configs import ScreenshotAgentConfig, VideoInterpreterConfig
from videoinstruct.agents.VideoInterpreter import VideoInterpreter
from videoinstruct.tools.video_screenshot import VideoScreenshotTool
from videoinstruct.tools.image_annotator import ImageAnnotatorTool


class ScreenshotAgent:
    """
    A class for extracting, annotating, and integrating screenshots into Markdown documentation.
    
    This class handles:
    1. Identifying screenshot placeholders in Markdown files
    2. Requesting timestamps from VideoInterpreter
    3. Extracting screenshots from videos
    4. Annotating screenshots using Gemini API
    5. Integrating annotated screenshots into Markdown files
    """
    
    def __init__(
        self,
        config: Optional[ScreenshotAgentConfig] = None,
        video_interpreter: Optional[VideoInterpreter] = None,
        video_path: Optional[str] = None,
        output_dir: str = "output"
    ):
        """
        Initialize the ScreenshotAgent.
        
        Args:
            config: Configuration for the Gemini model, including API key.
            video_interpreter: Pre-instantiated VideoInterpreter agent.
            video_path: Path to the video file.
            output_dir: Directory to save the annotated screenshots.
        """
        self.config = config or ScreenshotAgentConfig()
        self.video_interpreter = video_interpreter
        self.video_path = video_path
        self.output_dir = output_dir
        # Counter for screenshot numbering
        self.screenshot_counter = 1
        
        # Get API key from config or environment variable
        self.api_key = self.config.api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided in config or set as GEMINI_API_KEY environment variable")
        
        # Initialize Gemini client - set the API key
        genai.api_key = self.api_key
        
        # Configure the model with system instruction
        generation_config = {
            "temperature": self.config.temperature,
        }
        
        if self.config.max_output_tokens:
            generation_config["max_output_tokens"] = self.config.max_output_tokens
        if self.config.top_p:
            generation_config["top_p"] = self.config.top_p
        if self.config.top_k:
            generation_config["top_k"] = self.config.top_k
        if self.config.seed:
            generation_config["seed"] = self.config.seed
        
        print(f"Initializing Screenshot Agent with model: {self.config.model}")
        print(f"System instruction length: {len(self.config.system_instruction)} characters")
            
        self.model = genai.GenerativeModel(
            model_name=self.config.model,
            generation_config=generation_config,
            system_instruction=self.config.system_instruction
        )
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def set_video_path(self, video_path: str) -> None:
        """
        Set the video file path.
        
        Args:
            video_path: Path to the video file.
        """
        self.video_path = video_path
    
    def set_video_interpreter(self, video_interpreter: VideoInterpreter) -> None:
        """
        Set the VideoInterpreter agent.
        
        Args:
            video_interpreter: Pre-instantiated VideoInterpreter agent.
        """
        self.video_interpreter = video_interpreter
    
    def process_markdown_file(self, file_path: str) -> str:
        """
        Process a markdown file, replacing screenshot placeholders with actual annotated screenshots.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            Path to the enhanced markdown file
        """
        try:
            print(f"Processing markdown file: {file_path}")
            
            # Reset screenshot counter when processing a new file
            self.screenshot_counter = 1
            
            # Read the markdown file
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Fix indentation issues by stripping leading whitespace from each line
            lines = content.split('\n')
            fixed_lines = [line.lstrip() for line in lines]
            content = '\n'.join(fixed_lines)
            
            # Fix headers that might not have proper spacing
            content = re.sub(r'^(#+)(\S)', r'\1 \2', content, flags=re.MULTILINE)
            
            # Remove any triple backticks around image markdown to prevent images from being inside code blocks
            content = re.sub(r'```(?:.*?)\s*\n(!\[.*?\]\(.*?\))\s*\n```', r'\1', content)
            content = re.sub(r'```(?:.*?)(!\[.*?\]\(.*?\))```', r'\1', content)
            
            # Define regex pattern to identify screenshot placeholders in the format:
            # [SCREENSHOT_PLACEHOLDER]...[/SCREENSHOT_PLACEHOLDER]
            pattern = r'\[SCREENSHOT_PLACEHOLDER\](.*?)\[/SCREENSHOT_PLACEHOLDER\]'
            
            # Find all matches
            matches = re.findall(pattern, content, re.DOTALL)
            
            print(f"Found {len(matches)} screenshot placeholders")
            
            # Process each match
            for idx, placeholder_content in enumerate(matches):
                try:
                    # Parse the placeholder content to extract description
                    description = placeholder_content.strip()
                    
                    # Extract purpose, content, and value if available
                    purpose_match = re.search(r'Purpose:\s*(.*?)(?:\n|$)', placeholder_content)
                    content_match = re.search(r'Content:\s*(.*?)(?:\n|$)', placeholder_content)
                    value_match = re.search(r'Value:\s*(.*?)(?:\n|$)', placeholder_content)
                    
                    # Combine the extracted information into a description
                    description_parts = []
                    if purpose_match:
                        description_parts.append(purpose_match.group(1).strip())
                    if content_match:
                        description_parts.append(content_match.group(1).strip())
                    if value_match:
                        description_parts.append(value_match.group(1).strip())
                    
                    if description_parts:
                        description = " - ".join(description_parts)
                    
                    # Generate a timestamp based on the index (5 seconds apart)
                    timestamp = str((idx + 1) * 5)
                    
                    # Get timestamp from VideoInterpreter if available
                    if self.video_interpreter:
                        try:
                            timestamp_hms = self._get_timestamp_from_interpreter(description)
                            # Convert HH:MM:SS to seconds
                            h, m, s = map(int, timestamp_hms.split(':'))
                            timestamp = str(h * 3600 + m * 60 + s)
                        except Exception as e:
                            print(f"Error getting timestamp from interpreter: {str(e)}")
                    
                    # Check if screenshot already exists
                    screenshot_path = self._get_screenshot_path()
                    
                    if not os.path.exists(screenshot_path):
                        # Extract timestamp from VideoInterpreter
                        timestamp_seconds = int(timestamp)
                        
                        # Take screenshot using our own method instead of VideoInterpreter
                        screenshot_path = self.take_screenshot(timestamp_seconds)
                        
                        if not screenshot_path or not os.path.exists(screenshot_path):
                            print(f"Warning: Failed to take screenshot at timestamp {timestamp_seconds}")
                            continue
                    
                    # Annotate screenshot with description
                    annotated_path = self._annotate_screenshot(screenshot_path, description)
                    
                    if not annotated_path or not os.path.exists(annotated_path):
                        print(f"Warning: Failed to annotate screenshot for description: {description}")
                        continue
                    
                    # Get relative path for markdown
                    rel_path = os.path.relpath(annotated_path, os.path.dirname(file_path))
                    
                    # Replace placeholder with actual image in markdown
                    placeholder = f'[SCREENSHOT_PLACEHOLDER]{placeholder_content}[/SCREENSHOT_PLACEHOLDER]'
                    replacement = f'![{description}]({rel_path})'
                    content = content.replace(placeholder, replacement)
                    
                    print(f"Processed screenshot #{self.screenshot_counter}: {description} at timestamp {timestamp}")
                    # Increment the counter for the next screenshot
                    self.screenshot_counter += 1
                except Exception as e:
                    print(f"Error processing screenshot placeholder #{idx+1}: {str(e)}")
            
            # Ensure images are not inside code blocks by moving them outside
            # Find all code blocks
            code_blocks = re.finditer(r'```.*?```', content, re.DOTALL)
            for block in code_blocks:
                block_content = block.group(0)
                # Check if there are any images in this code block
                images = re.findall(r'!\[.*?\]\(.*?\)', block_content)
                if images:
                    # For each image found in the code block
                    for img in images:
                        # Remove the image from the code block
                        new_block = block_content.replace(img, '')
                        # Place the image after the code block
                        content = content.replace(block_content, new_block + '\n\n' + img)
            
            # Save the updated markdown to a new file
            filename_without_ext = os.path.splitext(file_path)[0]
            enhanced_file_path = f"{filename_without_ext}_enhanced.md"
            
            with open(enhanced_file_path, 'w') as f:
                f.write(content)
            
            print(f"Enhanced markdown saved to: {enhanced_file_path}")
            
            return enhanced_file_path
        except Exception as e:
            print(f"Error in process_markdown_file: {str(e)}")
            return file_path  # Return original file path if processing fails
    
    def _get_timestamp_from_interpreter(self, screenshot_description: str) -> str:
        """
        Get the timestamp for a screenshot from the VideoInterpreter.
        
        Args:
            screenshot_description: Description of what should be in the screenshot.
            
        Returns:
            Timestamp in HH:MM:SS format.
        """
        prompt = f"""
        I need to find a specific frame in the video that shows:
        
        {screenshot_description}
        
        Please provide the exact timestamp (in HH:MM:SS format) where this appears in the video.
        Only respond with the timestamp in HH:MM:SS format.
        """
        
        # Get response from VideoInterpreter
        response = self.video_interpreter.respond(prompt)
        
        # Extract timestamp using regex (looking for HH:MM:SS format)
        timestamp_pattern = r'(\d{1,2}):(\d{2}):(\d{2})'
        match = re.search(timestamp_pattern, response)
        
        if match:
            hours, minutes, seconds = match.groups()
            return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        else:
            # If no timestamp found, try to parse the response as a timestamp
            parts = response.strip().split(':')
            if len(parts) == 3 and all(part.isdigit() for part in parts):
                hours, minutes, seconds = parts
                return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
            
            # Default to beginning of video if no timestamp found
            print(f"Warning: Could not extract timestamp from response: {response}")
            return "00:00:05"  # Default to 5 seconds into the video
    
    def take_screenshot(self, timestamp_seconds: int) -> str:
        """
        Take a screenshot from the video at the specified timestamp and save it to disk.
        
        Args:
            timestamp_seconds: Timestamp in seconds
            
        Returns:
            Path to the saved screenshot
        """
        try:
            # Convert seconds to HH:MM:SS format
            hours = timestamp_seconds // 3600
            minutes = (timestamp_seconds % 3600) // 60
            seconds = timestamp_seconds % 60
            timestamp_hms = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            # Get the screenshot path
            screenshot_path = self._get_screenshot_path()
            
            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            
            # Extract the screenshot using VideoScreenshotTool
            screenshot = VideoScreenshotTool(self.video_path, timestamp_hms)
            
            # Save the screenshot
            screenshot.save(screenshot_path)
            
            print(f"Screenshot saved to {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"Error taking screenshot at {timestamp_seconds} seconds: {str(e)}")
            return None
    
    def _extract_screenshot(self, timestamp: str) -> Image.Image:
        """
        Extract a screenshot from the video at the specified timestamp.
        
        Args:
            timestamp: Timestamp in HH:MM:SS format.
            
        Returns:
            PIL Image object of the screenshot.
        """
        try:
            screenshot = VideoScreenshotTool(self.video_path, timestamp)
            return screenshot
        except Exception as e:
            raise Exception(f"Error extracting screenshot at {timestamp}: {str(e)}")
    
    def _annotate_screenshot(self, screenshot_path: str, description: str) -> str:
        """
        Annotate a screenshot using Gemini API and the Image Annotator tool.
        Also uses mamasight to pre-annotate the image for better Gemini performance.
        
        Args:
            screenshot_path: Path to the screenshot image.
            description: Description of what should be in the screenshot.
            
        Returns:
            Path to the annotated screenshot.
        """
        try:
            # Create a directory for annotated screenshots if it doesn't exist
            annotated_dir = os.path.join(self.output_dir, "screenshots")
            os.makedirs(annotated_dir, exist_ok=True)
            
            # Define the output filename using the screenshot number
            filename = os.path.basename(screenshot_path)
            filename = f"annotated_{filename}"
            annotated_path = os.path.join(annotated_dir, filename)
            
            # If the file already exists, return its path without regenerating
            if os.path.exists(annotated_path):
                return annotated_path
            
            # Load the screenshot image
            screenshot = Image.open(screenshot_path)
            img_width, img_height = screenshot.size
            
            # Try to use mamasight to pre-annotate the image if it's available
            try:
                from mamasight import ScreenParser
                from videoinstruct.tools.image_annotator import (
                    get_annotated_elements,
                    convert_bbox_mamasight_to_gemini
                )
                
                # Initialize parser with custom settings
                box_config = {
                    'box_overlay_ratio': 3200,
                    'text_scale': 1.0,
                    'text_thickness': 3,
                    'text_padding': 5,
                    'thickness': 4,
                    'annotation_style': 'simple',
                }
                
                # Create parser instance
                parser = ScreenParser(box_config=box_config)
                parser.setup(yolo_device='cpu', ocr_device=None)
                
                # Get annotated image, detections, and image dimensions
                annotated_image, detections, img_dimensions = get_annotated_elements(screenshot_path, parser)
                
                # Save temporary annotated image for Gemini
                temp_annotated_path = os.path.join(self.output_dir, f"temp_annotated_{filename}")
                try:
                    if annotated_image is not None:
                        print(f"Saving annotated image, shape: {annotated_image.shape}, type: {type(annotated_image)}")
                        success = cv2.imwrite(temp_annotated_path, annotated_image)
                        if not success:
                            print(f"Warning: cv2.imwrite returned False when saving {temp_annotated_path}")
                    else:
                        print("Warning: annotated_image is None, cannot save")
                except Exception as e:
                    print(f"Error saving annotated image: {str(e)}")
                    # If we can't save the annotated image, continue without it
                    # Use the original screenshot for further processing
                    temp_annotated_path = screenshot_path
                
                # Convert detections to a format suitable for the prompt
                ui_elements = []
                
                if not detections.empty:
                    for _, row in detections.iterrows():
                        if 'bbox' in row and isinstance(row['bbox'], list) and len(row['bbox']) == 4:
                            # Convert bbox from mamasight format to Gemini format
                            bbox_gemini = convert_bbox_mamasight_to_gemini(
                                row['bbox'], 
                                img_dimensions['width'], 
                                img_dimensions['height']
                            )
                            
                            ui_elements.append({
                                'box_id': row.get('box_id', f"element_{len(ui_elements)}"),
                                'box_type': row.get('box_type', 'unknown'),
                                'box_2d': bbox_gemini,  # Use Gemini's box_2d format
                                'confidence': row.get('confidence', 0.0),
                            })
                
                # Convert ui_elements to string for the prompt
                ui_elements_str = str(ui_elements) if ui_elements else "[]"
                
                # Load both original and annotated images for Gemini
                screenshot_annotated = None
                try:
                    if os.path.exists(temp_annotated_path):
                        screenshot_annotated = Image.open(temp_annotated_path)
                    else:
                        print(f"Warning: Annotated image file not found: {temp_annotated_path}")
                        # Use original image as fallback
                        screenshot_annotated = screenshot
                except Exception as e:
                    print(f"Error loading annotated image: {str(e)}")
                    # Use original image as fallback
                    screenshot_annotated = screenshot
                
                # Convert both images to base64
                buffered_orig = BytesIO()
                screenshot.save(buffered_orig, format="JPEG")
                img_str_orig = base64.b64encode(buffered_orig.getvalue()).decode()
                
                buffered_anno = BytesIO()
                screenshot_annotated.save(buffered_anno, format="JPEG")
                img_str_anno = base64.b64encode(buffered_anno.getvalue()).decode()
                
                # Update the prompt to include the pre-annotated image and detected UI elements
                prompt = f"""
                Annotate this screenshot showing: {description}
                
                I'm providing you with:
                1. The original screenshot
                2. The same screenshot with auto-detected UI elements highlighted
                3. A list of detected UI elements with their bounding boxes
                
                Detected UI elements:
                {ui_elements_str}
                
                Using this pre-annotation data, return a Python list of dictionaries with bounding boxes for important elements.
                Focus on elements that are relevant to the description.
                
                Each dictionary should have:
                - 'box_2d': [y_min, x_min, y_max, x_max] coordinates normalized from 0-1000
                - 'label': short description (2-5 words) of what this element is
                
                Example format:
                [
                    {{"box_2d": [100, 200, 300, 400], "label": "Search bar"}},
                    {{"box_2d": [500, 600, 700, 800], "label": "Navigation menu"}}
                ]
                """
                
                # Get annotations from Gemini with both images
                response = self.model.generate_content([
                    prompt,
                    {"mime_type": "image/jpeg", "data": img_str_orig},
                    {"mime_type": "image/jpeg", "data": img_str_anno}
                ])
                
                # Clean up temporary file
                if os.path.exists(temp_annotated_path):
                    os.remove(temp_annotated_path)
                    
            except ImportError:
                # If mamasight is not available, fallback to the original approach
                print("Mamasight package not available, using basic annotation only")
                
                # Convert the image to base64
                buffered = BytesIO()
                screenshot.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                
                # Prepare a prompt for Gemini
                prompt = f"""
                Annotate this screenshot showing: {description}
                
                Return ONLY a Python list of dictionaries with bounding boxes for important elements.
                Each dictionary should have:
                - 'box_2d': [y_min, x_min, y_max, x_max] coordinates normalized from 0-1000
                - 'label': short description (2-5 words) for each element
                
                Example format:
                [
                    {{"box_2d": [100, 200, 300, 400], "label": "Search bar"}},
                    {{"box_2d": [500, 600, 700, 800], "label": "Navigation menu"}}
                ]
                """
                
                # Get annotations from Gemini
                response = self.model.generate_content([
                    prompt, 
                    {"mime_type": "image/jpeg", "data": img_str}
                ])
            
            # Extract the list of dictionaries from the response
            try:
                # First try to find a Python code block
                code_pattern = r'```(?:python|json)?\s*(.*?)\s*```'
                code_match = re.search(code_pattern, response.text, re.DOTALL)
                
                if code_match:
                    bounding_boxes_str = code_match.group(1).strip()
                else:
                    # If no code block, try to extract the list directly
                    list_pattern = r'\[\s*{.*}\s*\]'
                    list_match = re.search(list_pattern, response.text, re.DOTALL)
                    if list_match:
                        bounding_boxes_str = list_match.group(0)
                    else:
                        # If still no match, use the entire response
                        bounding_boxes_str = response.text.strip()
                
                # Parse the string to get the list of dictionaries
                bounding_boxes = ast.literal_eval(bounding_boxes_str)
                
                # Import conversion function
                from videoinstruct.tools.image_annotator import convert_bbox_gemini_to_mamasight
                
                # Format the bounding boxes for ImageAnnotatorTool
                formatted_boxes = []
                for box in bounding_boxes:
                    new_box = {}
                    
                    # Handle box_2d format from Gemini
                    if 'box_2d' in box:
                        # Convert Gemini format to mamasight format
                        gemini_bbox = box['box_2d']
                        mamasight_bbox = convert_bbox_gemini_to_mamasight(gemini_bbox, img_width, img_height)
                        new_box['bbox'] = mamasight_bbox
                    
                    # Set id, color, and description
                    new_box['id'] = chr(65 + len(formatted_boxes))  # A, B, C, ...
                    new_box['color'] = 'red'
                    
                    if 'label' in box:
                        new_box['description'] = box['label']
                    elif 'description' in box:
                        new_box['description'] = box['description']
                    else:
                        new_box['description'] = f"Element {new_box['id']}"
                    
                    formatted_boxes.append(new_box)
                
                # Apply the annotations using ImageAnnotatorTool
                result = ImageAnnotatorTool(
                    image_path=screenshot_path,
                    bounding_boxes=formatted_boxes
                )
                
                # Save the annotated image
                try:
                    if result is not None:
                        print(f"Saving final annotated image, shape: {result.shape}, type: {type(result)}")
                        success = cv2.imwrite(annotated_path, result)
                        if not success:
                            print(f"Warning: cv2.imwrite returned False when saving {annotated_path}")
                            # Fall back to copying the original image
                            shutil.copy(screenshot_path, annotated_path)
                            print(f"Copied original image to {annotated_path} as fallback")
                    else:
                        print("Warning: result is None, cannot save")
                        # Fall back to the original screenshot
                        shutil.copy(screenshot_path, annotated_path)
                except Exception as e:
                    print(f"Error saving final annotated image: {str(e)}")
                    # Fall back to the original screenshot
                    shutil.copy(screenshot_path, annotated_path)
                
                return annotated_path
                
            except Exception as e:
                print(f"Error processing annotation response: {str(e)}")
                
                # Create a simple default annotation if parsing fails
                img = cv2.imread(screenshot_path)
                h, w = img.shape[:2]
                result = ImageAnnotatorTool(
                    image_path=screenshot_path,
                    bounding_boxes=[
                        {
                            'bbox': [w//4, h//4, 3*w//4, 3*h//4],
                            'color': 'red',
                            'id': 'A',
                            'description': 'Main content'
                        }
                    ]
                )
                
                # Save the annotated image
                try:
                    if result is not None:
                        print(f"Saving default annotated image, shape: {result.shape}, type: {type(result)}")
                        success = cv2.imwrite(annotated_path, result)
                        if not success:
                            print(f"Warning: cv2.imwrite returned False when saving default annotation to {annotated_path}")
                            # Fall back to copying the original image
                            shutil.copy(screenshot_path, annotated_path)
                            print(f"Copied original image to {annotated_path} as fallback")
                    else:
                        print("Warning: default result is None, cannot save")
                        # Fall back to the original screenshot
                        shutil.copy(screenshot_path, annotated_path)
                except Exception as e:
                    print(f"Error saving default annotated image: {str(e)}")
                    # Fall back to the original screenshot
                    shutil.copy(screenshot_path, annotated_path)
                
                return annotated_path
                
        except Exception as e:
            print(f"Error annotating screenshot: {str(e)}")
            return screenshot_path  # Return original screenshot path if annotation fails
    
    def _get_screenshot_path(self) -> str:
        """
        Get the path for a screenshot based on the sequential counter.
        
        Returns:
            Path to the screenshot file
        """
        # Create a directory for screenshots if it doesn't exist
        screenshots_dir = os.path.join(self.output_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        
        # Define the screenshot path using the counter for sequential numbering
        return os.path.join(screenshots_dir, f"screenshot_{self.screenshot_counter}.png")


# Example usage
if __name__ == "__main__":
    print("Running ScreenshotAgent example...")
    
    # Create a simple markdown file with screenshot placeholders
    parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    temp_dir = os.path.join(parent_dir, "temp")
    os.makedirs(temp_dir, exist_ok=True)
    
    markdown_content = """# Radiographics Tutorial
    ## Step 1: Search for Articles
    [SCREENSHOT_PLACEHOLDER]
    Purpose: Shows a Google search result with "Radiographics Top 10 Articles" query
    Content: The search results page with the RG TEAM Top 10 Reading List appearing as the top result
    Value: Helps the user identify the correct search query and result to click
    [/SCREENSHOT_PLACEHOLDER]

    ## Step 2: Access the Website
    [SCREENSHOT_PLACEHOLDER]
    Purpose: Shows the Radiographics website homepage
    Content: The main landing page with navigation menu and featured articles
    Value: Helps the user understand what the website looks like and how to navigate it
    [/SCREENSHOT_PLACEHOLDER]
    """
    
    temp_md_path = os.path.join(temp_dir, "tutorial.md")
    with open(temp_md_path, "w") as f:
        f.write(markdown_content)
    
    print(f"Created temporary markdown file: {temp_md_path}")
    
    # Video Path - use a command line argument if provided, otherwise use default
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
    else:
        # Default video path
        video_path = os.path.join(parent_dir, "data", "RG_Drive_Demonsration.mp4")
    
    print(f"Using video: {video_path}")
    
    # Initialize the VideoInterpreter
    print("Initializing VideoInterpreter...")
    video_interpreter = VideoInterpreter()
    video_interpreter.load_video(video_path)
    
    # Initialize the ScreenshotAgent
    print("Initializing ScreenshotAgent...")
    output_dir = os.path.join(os.path.dirname(temp_md_path), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    screenshot_agent = ScreenshotAgent(
        video_interpreter=video_interpreter, 
        video_path=video_path,
        output_dir=output_dir
    )

    # Process the Markdown file
    print("Processing markdown file...")
    enhanced_markdown_path = screenshot_agent.process_markdown_file(temp_md_path)
    print(f"Enhanced Markdown saved to: {enhanced_markdown_path}")
    print(f"Screenshots saved in: {os.path.join(output_dir, os.path.basename(temp_md_path).split('.')[0] + '_screenshots')}")
    
    # Run it again to demonstrate screenshot reuse
    print("\nProcessing markdown file again to demonstrate screenshot reuse...")
    enhanced_markdown_path = screenshot_agent.process_markdown_file(temp_md_path)
    print(f"Enhanced Markdown saved to: {enhanced_markdown_path}")
    print(f"Existing screenshots were reused instead of being regenerated.")
    
    print("\nTo run this example with a different video:")
    print(f"python {__file__} /path/to/your/video.mp4")

