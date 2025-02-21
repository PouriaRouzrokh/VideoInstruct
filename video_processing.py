from contextlib import redirect_stdout, redirect_stderr
from moviepy.video.io.VideoFileClip import VideoFileClip
import numpy as np
import os
from PIL import Image

def get_video_screenshot(video_path, time_str):
    """
    Extract a screenshot from a video at a specific timestamp.
    
    Args:
        video_path (str): Path to the MP4 video file
        time_str (str): Timestamp in "MM:SS" format
        
    Returns:
        PIL.Image: Screenshot image at the specified timestamp
        
    Example:
        screenshot = get_video_screenshot("my_video.mp4", "02:45")
        screenshot.save("screenshot.jpg")
    """
    # Check if file exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    # Parse the time string to get seconds
    try:
        minutes, seconds = map(int, time_str.split(':'))
        time_seconds = minutes * 60 + seconds
    except ValueError:
        raise ValueError("Time must be in 'MM:SS' format")
    
    try:
        # Load the video silently
        with open(os.devnull, 'w') as devnull:
            with redirect_stdout(devnull), redirect_stderr(devnull):
                clip = VideoFileClip(video_path)
        
        # Check if the requested time exceeds video duration
        if time_seconds > clip.duration:
            raise ValueError(f"Requested time {time_str} exceeds video duration of {int(clip.duration // 60):02d}:{int(clip.duration % 60):02d}")
        
        # Get the frame at the specified time
        with open(os.devnull, 'w') as devnull:
            with redirect_stdout(devnull), redirect_stderr(devnull):
                frame = clip.get_frame(time_seconds)
        
        # Convert the numpy array to a PIL Image
        screenshot = Image.fromarray(np.uint8(frame))
        
        # Close the video file
        clip.close()
        
        return screenshot
    
    except Exception as e:
        raise Exception(f"Error extracting screenshot: {str(e)}")


# Example usage
if __name__ == "__main__":

    screenshot = get_video_screenshot("test/test.mp4", "00:10")
    screenshot.save("test/screenshot.jpg")
