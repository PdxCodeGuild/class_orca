
# uses pillow to import an image
from PIL import Image
# sets a reference for the image to use
img = Image.open("lenna.png")
# defines the dimensions of the image as variables
width, height = img.size
# processes the data of the image to be read
pixels = img.load()

# singles out indivdual pixels and identifies each pixel's RBG value
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        
        # a formula to covert RBG value to greyscale
        y = int(0.299*r) + int(0.587*g) + int(0.114*b)

        # replaces the original RGB value with the new greyscale value
        pixels[i, j] = (y, y, y)

# displays image
img.show()