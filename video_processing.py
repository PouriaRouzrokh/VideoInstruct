from contextlib import redirect_stdout, redirect_stderr
from moviepy.video.io.VideoFileClip import VideoFileClip
import numpy as np
import os
from PIL import Image
import sys

class VideoScreenshotExtractor:
    """
    A class to extract screenshots from video files at specific timestamps.
    """
    
    def __init__(self, video_path):
        """
        Initialize with a video file path.
        
        Args:
            video_path (str): Path to the MP4 video file
        """
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
            
        self.video_path = video_path

        # Temporarily redirect stdout and stderr to devnull to silence moviepy
        with open(os.devnull, 'w') as devnull:
            with redirect_stdout(devnull), redirect_stderr(devnull):
                self.clip = VideoFileClip(video_path)
        
    def get_screenshot(self, time_str):
        """
        Extract a screenshot at a specific timestamp.
        
        Args:
            time_str (str): Timestamp in "MM:SS" format
            
        Returns:
            PIL.Image: Screenshot image at the specified timestamp
        """
        # Parse the time string to get seconds
        try:
            minutes, seconds = map(int, time_str.split(':'))
            time_seconds = minutes * 60 + seconds
        except ValueError:
            raise ValueError("Time must be in 'MM:SS' format")
        
        # Check if the requested time exceeds video duration
        if time_seconds > self.clip.duration:
            raise ValueError(f"Requested time {time_str} exceeds video duration of {int(self.clip.duration // 60):02d}:{int(self.clip.duration % 60):02d}")
        
        # Get the frame at the specified time
        # Temporarily redirect stdout and stderr to devnull to silence moviepy
        with open(os.devnull, 'w') as devnull:
            with redirect_stdout(devnull), redirect_stderr(devnull):
                frame = self.clip.get_frame(time_seconds)
        
        # Convert the numpy array to a PIL Image
        screenshot = Image.fromarray(np.uint8(frame))
        
        return screenshot
    
    def close(self):
        """Close the video file to free resources"""
        if hasattr(self, 'clip') and self.clip:
            self.clip.close()
    
    def __del__(self):
        """Destructor to ensure video file is closed"""
        self.close()


# Example usage
if __name__ == "__main__":

    extractor = VideoScreenshotExtractor("test/test.mp4")
    screenshot = extractor.get_screenshot("00:10")
    screenshot.save("test/screenshot.jpg")
    extractor.close()