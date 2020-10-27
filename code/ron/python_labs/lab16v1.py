
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab16v1
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-14-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 16v1: Image Manipulation

'''
#----Modules------------------------------------------------

from PIL import Image

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

            # Change RGB to greyscale via Y variable formula
            Y = int(0.299 * r) + int(0.587 * g) + int(0.114 * b)
            r = Y
            g = Y
            b = Y

            pixels[i, j] = (r, g, b)

    # Output
    img.show()

main()











