import os
from PIL import Image

folder = '/home/xxx/Desktop/xxx'

# Get a list of all the files in the folder
files = os.listdir(folder)

# Loop through each file in the folder
for file in files:
    # Check if the file is an image file
    if not file.endswith('.jpg') and not file.endswith('.jpeg') and not file.endswith('.png'):
        continue

    # Construct the full path to the file
    path = os.path.join(folder, file)

    # Open the image using the Python Imaging Library (PIL)
    image = Image.open(path)

    # Get the original size of the image
    width, height = image.size

    # Calculate the new size of the image
    new_height = 1080
    new_width = int(width * new_height / height)

    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # Save the resized image with the same file format
    resized_image.save(path)
