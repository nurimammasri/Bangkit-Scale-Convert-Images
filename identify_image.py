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
