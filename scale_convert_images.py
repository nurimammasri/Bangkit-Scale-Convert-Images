#!/usr/bin/env python3
import os
from PIL import Image

destinationDirectory = os.path.join("opt", "icons", "")
imagesDirectory = os.path.join("images", "")


def create_destination():
    """Make directory for destination /opt/icons/"""
    # check if directory already created
    if not os.path.exists(destinationDirectory):
        os.makedirs(destinationDirectory)


def manipulate_image(infile):
    """Manipulate Image File
    - Rotate the image 90° clockwise
    - Resize the image from 192x192 to 128x128
    - Save the image to a new folder in .jpeg format"""

    # declares a location image and a new image location
    image_loc = os.path.join(imagesDirectory, infile)
    newimage_loc = os.path.join(destinationDirectory, infile)

    # make exception handle for manipulating image
    try:
        with Image.open(image_loc) as img:
            image = img.rotate(-90).resize((128, 128)).convert("RGB")
            image.save(newimage_loc + ".jpeg", "JPEG")
    except OSError:
        print("cannot convert", infile)


def prosessing_image():
    """Iterates over the file name in the directory"""
    # looping through on name file
    # os.listdir to list all file on directory
    for infile in os.listdir(imagesDirectory):
        # continue when .DS_Store file
        if infile.startswith('.'):
            continue
        manipulate_image(infile)


if __name__ == '__main__':
    create_destination()
    prosessing_image()
