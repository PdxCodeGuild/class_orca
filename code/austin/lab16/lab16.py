#Lab16: Change to Greyscale

from PIL import Image
img = Image.open("test_image.jpg")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i,j]
        y = 0.299 * r + 0.587 * g + 0.114 * b

        r = int(y)
        g = int(y)
        b = int(y)


        pixels[i,j] = (r, g, b)

img.show()