import os
from moviepy.editor import *

# directory containing the videos
video_dir = "C:\Users\xxx\Documents\xxx"

# list of videos to be processed
video_list = [os.path.join(video_dir, f) for f in os.listdir(video_dir) if f.endswith(".mp4")]

for video in video_list:
    clip = VideoFileClip(video)
    clip.fps = 30
    clip.write_videofile(video)
