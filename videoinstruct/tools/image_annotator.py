import cv2
import numpy as np
from typing import List, Dict, Union, Tuple, Optional


def ImageAnnotatorTool(
    image_path: str,
    bounding_boxes: List[Dict[str, Union[List[int], str]]],
    settings: Optional[Dict[str, Union[int, str, float]]] = None
) -> np.ndarray:
    """
    Annotate an image with bounding boxes, IDs, and arrows connecting boxes.
    
    Args:
        image_path (str): Path to the input image file.
        bounding_boxes (List[Dict]): List of dictionaries, each containing:
            - 'bbox' (List[int]): Bounding box coordinates [x1, y1, x2, y2].
            - 'color' (str): Color name for the bounding box (e.g., 'red', 'green').
            - 'id' (str): ID label for the bounding box (e.g., 'A', 'B', 'C').
            - 'description' (str, optional): Description text to display next to the bounding box.
            - 'destination_id' (str, optional): ID of the box to connect to with an arrow.
        settings (Dict, optional): Configuration settings including:
            - 'line_thickness' (int): Thickness of bounding box lines (default: 2).
            - 'text_scale' (float): Scale of text (default: 0.7).
            - 'text_thickness' (int): Thickness of text (default: 2).
            - 'arrow_color' (str): Color for arrows (default: 'blue').
            - 'arrow_thickness' (int): Thickness of arrows (default: 2).
            - 'arrow_tip_length' (float): Length of arrow tip (default: 0.03).
            - 'description_offset' (int): Vertical offset for description text (default: 15).
    
    Returns:
        np.ndarray: Annotated image as a NumPy array.
    """
    # Default settings
    default_settings = {
        'line_thickness': 2,
        'text_scale': 0.7,
        'text_thickness': 2,
        'arrow_color': 'blue',
        'arrow_thickness': 2,
        'arrow_tip_length': 0.1,
        'description_offset': 15
    }
    
    # Update default settings with provided settings
    if settings is None:
        settings = {}
    for key, value in default_settings.items():
        if key not in settings:
            settings[key] = value
    
    # Color mapping
    color_map = {
        'red': (0, 0, 255),
        'green': (0, 255, 0),
        'blue': (255, 0, 0),
        'yellow': (0, 255, 255),
        'purple': (255, 0, 255),
        'cyan': (255, 255, 0),
        'white': (255, 255, 255),
        'black': (0, 0, 0)
    }
    
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image from {image_path}")
    
    # Create a mapping from ID to bounding box info for arrow connections
    id_to_bbox = {}
    for box in bounding_boxes:
        if 'id' in box:
            id_to_bbox[box['id']] = box
    
    # Draw bounding boxes and IDs
    for box in bounding_boxes:
        # Extract box information
        bbox = box.get('bbox', [0, 0, 0, 0])
        color_name = box.get('color', 'red')
        box_id = box.get('id', '')
        description = box.get('description', '')
        
        # Get color in BGR format
        color = color_map.get(color_name.lower(), (0, 0, 255))  # Default to red if color not found
        
        # Draw bounding box
        cv2.rectangle(
            image, 
            (bbox[0], bbox[1]), 
            (bbox[2], bbox[3]), 
            color, 
            settings['line_thickness']
        )
        
        # Draw ID text
        text_position = (bbox[0], bbox[1] - 10)
        cv2.putText(
            image,
            box_id,
            text_position,
            cv2.FONT_HERSHEY_SIMPLEX,
            settings['text_scale'],
            color,
            settings['text_thickness']
        )
        
        # Draw description text if provided
        if description:
            description_position = (bbox[0], bbox[3] + settings['description_offset'])
            cv2.putText(
                image,
                description,
                description_position,
                cv2.FONT_HERSHEY_SIMPLEX,
                settings['text_scale'],
                color,
                settings['text_thickness']
            )
    
    # Draw arrows
    for box in bounding_boxes:
        if 'destination_id' in box and box['destination_id'] in id_to_bbox:
            # Get source and destination boxes
            source_bbox = box['bbox']
            dest_box = id_to_bbox[box['destination_id']]
            dest_bbox = dest_box['bbox']
            
            # Define all corners of source bounding box
            source_corners = [
                (source_bbox[0], source_bbox[1]),  # top-left
                (source_bbox[2], source_bbox[1]),  # top-right
                (source_bbox[0], source_bbox[3]),  # bottom-left
                (source_bbox[2], source_bbox[3])   # bottom-right
            ]
            
            # Define all corners of destination bounding box
            dest_corners = [
                (dest_bbox[0], dest_bbox[1]),  # top-left
                (dest_bbox[2], dest_bbox[1]),  # top-right
                (dest_bbox[0], dest_bbox[3]),  # bottom-left
                (dest_bbox[2], dest_bbox[3])   # bottom-right
            ]
            
            # Find the closest pair of corners
            min_distance = float('inf')
            closest_source_corner = None
            closest_dest_corner = None
            
            for s_corner in source_corners:
                for d_corner in dest_corners:
                    # Calculate Euclidean distance between corners
                    distance = np.sqrt((s_corner[0] - d_corner[0])**2 + (s_corner[1] - d_corner[1])**2)
                    if distance < min_distance:
                        min_distance = distance
                        closest_source_corner = s_corner
                        closest_dest_corner = d_corner
            
            # Get arrow color
            arrow_color_name = settings.get('arrow_color', 'blue')
            arrow_color = color_map.get(arrow_color_name.lower(), (255, 0, 0))  # Default to blue
            
            # Draw arrow between the closest corners
            cv2.arrowedLine(
                image,
                closest_source_corner,
                closest_dest_corner,
                arrow_color,
                settings['arrow_thickness'],
                tipLength=settings['arrow_tip_length']
            )
    
    return image