import os
from PIL import Image

imagesDirectory = os.path.join("images", "")

for infile in os.listdir(imagesDirectory):
    image = os.path.join(imagesDirectory, infile)
    try:
        with Image.open(image) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass

"""
The images received are in the wrong format:
* .tiff format
* Image resolution 192x192 pixel (too large)
* Rotated 90° anti-clockwise

The images required for the launch should be in this format:

* .jpeg format

* Image resolution 128x128 pixel

* Should be straight
"""
