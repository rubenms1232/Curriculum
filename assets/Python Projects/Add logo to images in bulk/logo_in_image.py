from PIL import Image
import os

def add_logo(img, logo):
    # Open the image and logo
    image = Image.open(img)
    logo = Image.open(logo)

    # Resize the logo to be three times bigger
    logo = logo.resize((logo.width * 1, logo.height * 1))

    # Calculate the position of the logo
    image_width, image_height = image.size
    logo_width, logo_height = logo.size
    position = ((image_width - logo_width) // 2, (image_height - logo_height) // 2)

    # Add the logo to the image
    image.paste(logo, position, logo)
    return image


# Set the path to the images and logo
images_folder = "/home/xxx/Desktop/background"
logo_path = "/home/xxx/Desktop/logo.png"

# Get a list of all the images in the folder
images = [img for img in os.listdir(images_folder) if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png")]

# Add the logo to each image
for img in images:
    image_path = os.path.join(images_folder, img)
    image_with_logo = add_logo(image_path, logo_path)
    image_with_logo.save(image_path)
