import os
from moviepy.editor import *

# Directory containing the original videos
video_dir = r"C:\Users\xxx\Desktop\xxx\Videos"

# Directory to save the processed videos
output_dir = r"C:\Users\xxx\Desktop\xxx\Videosrender"

# Ensure the output directory exists, create it if necessary
os.makedirs(output_dir, exist_ok=True)

# List of videos to be processed
video_list = [os.path.join(video_dir, f) for f in os.listdir(video_dir) if f.endswith(".mp4")]

for video_path in video_list:
    video_name = os.path.basename(video_path)
    output_path = os.path.join(output_dir, video_name)

    clip = VideoFileClip(video_path)
    clip = clip.set_fps(30)  # Set the frame rate to 30 FPS
    clip.write_videofile(output_path)

print("Processing complete. Processed videos saved in:", output_dir)
