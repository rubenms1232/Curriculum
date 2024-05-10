import cv2
import os

# Specify the folder where the 720p videos are stored
folder = "/home/xxx/xxx"

# Loop through all the files in the folder
for filename in os.listdir(folder):
    # Check if the file is a video
    if filename.endswith(".mp4"):
        # Read the video
        cap = cv2.VideoCapture(os.path.join(folder, filename))

        # Get the dimensions of the frames in the video
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        # Get the framerate of the video
        framerate = int(cap.get(5))

        # Check if the video is 720p
        if frame_height == 720:
            # Define the scaling factor
            scale_factor = 1.5

            # Calculate the new dimensions for the frames
            new_frame_width = int(frame_width * scale_factor)
            new_frame_height = int(frame_height * scale_factor)

            # Define the codec and create the VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter("1080p_" + filename, fourcc, framerate, (new_frame_width, new_frame_height))

            # Loop through all the frames in the video
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    # Scale the frame
                    frame = cv2.resize(frame, (new_frame_width, new_frame_height))

                    # Write the frame to the output video
                    out.write(frame)
                else:
                    break

            # Release the VideoCapture and VideoWriter objects
            cap.release()
            out.release()
