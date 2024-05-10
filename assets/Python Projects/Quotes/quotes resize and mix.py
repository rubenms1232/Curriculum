import os
import cv2
import random

# Function to overlay input images on random backgrounds and save them
def overlay_images(input_folder, output_folder, background_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    input_images = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in input_images:
        try:
            # Load the input image
            input_image_path = os.path.join(input_folder, image_file)
            img = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)  # Load with alpha channel

            if img is None:
                print(f"Failed to load image: {input_image_path}")
                continue

            # Load a random background image
            background_files = [f for f in os.listdir(background_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
            random_background_file = random.choice(background_files)
            background_image_path = os.path.join(background_folder, random_background_file)
            background = cv2.imread(background_image_path)

            if background is None:
                print(f"Failed to load background image: {background_image_path}")
                continue

            # Resize the background to match the size of the input image
            background = cv2.resize(background, (img.shape[1], img.shape[0]))

            # Resize the overlay image by 5%
            scale_percent = 90  # 95% of the original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            img = cv2.resize(img, (width, height))

            # Calculate the position to center the overlay on the background
            x_offset = (background.shape[1] - img.shape[1]) // 2
            y_offset = (background.shape[0] - img.shape[0]) // 2

            # Overlay the input image on top of the background
            result = background.copy()
            alpha = img[:, :, 3] / 255.0  # Extract alpha channel and normalize
            for c in range(0, 3):
                result[y_offset:y_offset + img.shape[0], x_offset:x_offset + img.shape[1], c] = (1.0 - alpha) * background[y_offset:y_offset + img.shape[0], x_offset:x_offset + img.shape[1], c] + alpha * img[:, :, c]

            # Save the result in the output folder
            output_image_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_image_path, result)

            print(f"Processed: {input_image_path}")

        except Exception as e:
            print(f"Error processing image: {input_image_path}")
            print(str(e))

# Specify the input folder with images, output folder for processed images, and folder with background images
input_folder = r'C:\Users\xxx\Desktop\xxx\Quotesgreen'
output_folder = r'C:\Users\xxx\Desktop\xxx\Output'
background_folder = r'C:\Users\xxx\Desktop\xxx\Background'

overlay_images(input_folder, output_folder, background_folder)
