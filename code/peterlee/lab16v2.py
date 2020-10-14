import colorsys
import random

from PIL import Image


img = Image.open("Lenna_(test_image).png")
width, height = img.size
pixels = img.load()


for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        #shift hue by 180 and ensures it won't go over 1.0
        h = h + 0.5
        if h > 1.0:
            h - 1.0
        
        #increases saturation slightly and ensures it won't go over 1.0
        s = s ** 0.9

        r, g, b = colorsys.hsv_to_rgb(h, s, v)


        r = round(int(r*255) ** .8)
        g = round(int(g*255) ** .8)
        b = round(int(b*255) ** .8)

        pixels[i, j] = (r, g, b)



img.show()