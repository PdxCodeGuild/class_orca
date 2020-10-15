
# imports colorsys and the image with pillow. defines the image as img. defines dimensions. loads img to use as data
import colorsys
from PIL import Image
img = Image.open('Lenna.png')
height, width = img.size
pixels = img.load()

# targets each pixel for modification
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i,j]

        # converts each RGB value to HSV value
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        # increses hue and saturation and decreses brighness
        h = h*1.7
        s = s*2.3
        v = v*0.5

        # converts HSV back into RGB
        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # converts HSV [0,1] values back to RGB [0, 255] values
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        # assigns each pixel the new RGB value
        pixels[i, j] = (r, b, g)

# displays the now very freaky playboy lady
img.show()