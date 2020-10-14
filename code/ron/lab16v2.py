
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab16v2
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-14-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 16v2: Image Manipulation

'''
#----Modules------------------------------------------------

from PIL import Image
import colorsys

#----Global variables, lists, dictionaries------------------
''' none '''
#----Functions----------------------------------------------
''' none '''
#--------Main Code---------------------------------------------

def main(): 

    # Import image
    img = Image.open("lenna.png") # must be in same folder
    width, height = img.size
    pixels = img.load()

    # Loop through pixels
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # colorsys uses colors in the range [0, 1]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

            # H = Hue - rotate
            h = h * 1.5

            # S = Saturation - increase
            s = s * 2

            # V = Value/Brightness - decrease
            v = v - (v * .5)

            r, g, b = colorsys.hsv_to_rgb(h, s, v)

            # convert back to [0, 255]
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)

            pixels[i, j] = (r, g, b)

    # Output
    img.show()

main()



#----- Old code-------------------------------------------------------------------
            # # Change RGB to greyscale via Y variable formula
            # Y = int(0.299 * r) + int(0.587 * g) + int(0.114 * b)
            # r = Y
            # g = Y
            # b = Y






