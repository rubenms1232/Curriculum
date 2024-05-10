import os
import pandas as pd
from moviepy.editor import AudioFileClip, VideoFileClip, vfx

# Read the Excel file containing the locations of the .mp3 and .mp4 files
df = pd.read_excel("xxx.xlsx")

# Loop through each row in the dataframe
for i, row in df.iterrows():
    # Get the .mp3 and .mp4 file locations
    audio_path = row["mp3_location"]
    video_path = row["mp4_location"]

    # Set the output path to be the name of the song playing
    song_name = os.path.splitext(os.path.basename(audio_path))[0]
    output_path = row["song_name"] + ".mp4"

    try:
        # Create the audio and video clips
        audio_clip = AudioFileClip(audio_path)
        video_clip = VideoFileClip(video_path)

        # Set the fps to 25
        video_clip.fps = 30

        # Loop the video clip for the duration of the audio clip
        video_loop = vfx.loop(video_clip, duration=audio_clip.duration)

        # Set the audio of the video clip to be the audio clip
        video_loop = video_loop.set_audio(audio_clip)

        # Write the resulting video clip to the output path
        video_loop.write_videofile(output_path, fps=25)

        # Update the dataframe with the output path
        df.at[i, "output"] = output_path

    except Exception as e:
        print(f"An error occurred while processing row {i}: {str(e)}")

# Save the updated dataframe to an Excel file
df.to_excel("xxx.xlsx", index=False)
