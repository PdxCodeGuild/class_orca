
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab16v3
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-14-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 16v3: Image Manipulation

'''
#----Modules------------------------------------------------

from PIL import Image
import colorsys
from PIL import Image, ImageDraw, ImageFont


#----Global variables, lists, dictionaries------------------

moon_color = (254, 252, 215)
face_color = (224, 172, 105)
font = ImageFont.truetype(font="./fonts/creepsville.ttf", size=25)


#----Functions----------------------------------------------
''' none '''
#--------Main Code---------------------------------------------

def main(): 

    # Parameters and setup
    width = 500
    height = 500
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # origin (0, 0) is at the top-left corner
    # Sky
    draw.rectangle(((0, 0), (width, height)), fill="blue")
    # white box
    draw.rectangle(((0, 400), (width, height)), fill="white")
    # Grass
    draw.rectangle(((0, 400), (width, height)), fill="green")

    # x0, y0, x1, y1
    # Body
    draw.line((250, 320, 250, 380), fill="black")
    # Legs
    draw.line((250, 380, 225, 420), fill="black")
    draw.line((250, 380, 275, 420), fill="black")
    # Arms
    draw.line((250, 350, 225, 380), fill="black")
    draw.line((250, 350, 275, 380), fill="black")
    # Head
    draw.ellipse((225, 275, 275, 325), fill = face_color)
    # Face
    draw.ellipse((235, 305, 265, 315), fill='black')
    draw.ellipse((230, 295, 235, 300), fill='black')
    draw.ellipse((240, 295, 245, 300), fill='black')
    # Bats
    draw.line((100, 360, 90, 340), fill="black")
    draw.line((100, 360, 110, 340), fill="black")
    draw.ellipse((97, 360, 105, 365), fill='black')
    draw.line((130, 350, 120, 340), fill="black")
    draw.line((130, 350, 140, 340), fill="black")
    draw.ellipse((127, 350, 132, 355), fill='black')

    # Text
    message = "Happy Halloween"
    draw.text((160, 220), message, fill="orange", font=font)

    # Moon
    circle_x = width/4
    circle_y = height/4
    circle_radius = 50
    draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill = moon_color)
    
    # Output
    img.show()

main()






