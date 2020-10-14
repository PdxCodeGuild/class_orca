##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab16-image_manipulation.md
##############################################################################

            # http://colorizer.org/ useful

from PIL import Image # needed for all versions
import colorsys # needed for v2, to increase the saturation, decrease the brightness, and rotate the hue

file_to_open = 'lenna.png' # This line makes it slightly simpler to change the filename

# LAB VERSION 1, MAKES AN INPUT IMAGE INTO GREYSCALE (outputs to screen, but does not save file)

def greyscale(image,brightness=1): # requires from PIL import Image 
    # Brightness values as float percentages of original (so 1.3 is 130% or 30% increase; 0.6 is 60% or 40% decrease, etc...)

    image = Image.open(image)
    width, height = image.size # .size retuns a tuple, this sets those two variables as the two values
    pixels = image.load()

    for i in range(width):
        for j in range(height):

            # This would reduce brightness by 3:
            # r = int(r / 3)
            # g = int(g / 3)
            # b = int(b / 3)

            r, g, b = pixels[i, j] # tuple unpacking

            # STEP ONE Use this formula to get the brightness in Y from the RGB triplet
            # Y = 0.299*R + 0.587*G + 0.114*B
            # Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math will often use floats. 
            y = int( 0.299*r + 0.587*g + 0.114*b )
            y = y * brightness

            # STEP TWO Y is the brightness so set RGB to Y
            r = int(y)
            g = int(y)
            b = int(y)

            pixels[i, j] = (r, g, b)

    image.show()

brightness = 1.5 # Brightness values as float percentages of original (so 1.3 is 130% or 30% increase; 0.6 is 60% or 40% decrease, etc...)

# run it!
greyscale(file_to_open,brightness)

##############################################################################

# LAB VERSION 2, LETS YOU CHANGE THE HUE, SATURATION, AND BRIGHTNESS (outputs to screen, but does not save file)

def change_HSV(image,hue_new=1,sat_new=1,bri_new=1): # requires import colorsys, and from PIL import Image
    
    # NOTE Input Hue, Saturation, and Brightness values as float percentages of original (so 1.3 is 130% or 30% increase; 0.6 is 60% or 40% decrease, etc...)

    image = Image.open(image)
    width, height = image.size # .size retuns a tuple, this sets those two variables as the two values
    pixels = image.load()

    for i in range(width):
        for j in range(height):

            r, g, b = pixels[i, j] # tuple unpacking

            # Colorsys represents colors as floats in the range 0.0 - 1.0... 
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255) # Outputs floats 0-1 range

            h = h * hue_new
            s = s * sat_new
            v = v * bri_new

            # ...whereas pillow uses ints in the range 0 - 255. You'll have to convert between these two representations.            
            # NOTE I didn't convert anything, I think because I used percentages of the HSV values =)
            r, g, b = colorsys.hsv_to_rgb(h, s, v)

            # convert back to [0, 255]
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)

            pixels[i, j] = (r, g, b)

    image.show()

# VERSION 2: # do some math on h, s, v. Use the colorsys library to 
# Future could let user input these values, but would need integer/number/percent checks to ensure input was a percentage
    # STEP 3 and rotate the hue. 
hue_new = 1.5
    # STEP 1 increase the saturation, 
sat_new = 1.25
    # STEP 2 decrease the brightness, 
bri_new = 0.9

# run it!
change_HSV(file_to_open,hue_new,sat_new,bri_new)

##############################################################################


print('    >> PROGRAM ENDED <<    ')