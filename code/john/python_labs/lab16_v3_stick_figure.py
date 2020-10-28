##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab16-image_manipulation.md
##############################################################################

from PIL import Image, ImageDraw
from random import randint # only needed for random_draw below

def random_draw(width=100,height=100):

    ######### copied from merritt online
    ######### "Try running the code below, which generates 1000 random lines with random colors.""

    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    for i in range(1000):
        x0 = randint(0, width)
        y0 = randint(0, height)
        x1 = randint(0, width)
        y1 = randint(0, height)
        line_width = randint(1, 40)
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

    img.show()

# RUN IT!
# width = 1200
# height = 600
# random_draw(width,height)

# LAB VERSION 3, DRAW A STICK FIGURE (outputs to screen, but does not save file)

def draw_stick_figure(width=600,height=600):
    stick_figure = Image.new('RGB', (width, height))

    draw = ImageDraw.Draw(stick_figure)

    # the origin (0, 0) is at the top-left corner

    draw.rectangle(((0, 0), (width, height)), fill="white")

    # body 
    # draw a rectangle from x0, y0 to x1, y1
    draw.rectangle(((200, 200), (400, 500)), fill="yellow")

    color = (156, 228, 228)

    # arms
    draw.line((250,250,150,350), width=3, fill=color)
    draw.line((350,250,450,350), width=3, fill=color) 

    # legs
    draw.line((250,400,150,height), width=3, fill=color) # top left line to bottom right
    draw.line((350,400,450,height), width=3, fill=color) # top right to bottom left

    # head
    circle_x = 300 # width/2
    circle_y = 100 # height/2
    circle_radius = 100
    draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='red')

    # eyes
    draw.ellipse((250,50,275,75), fill='white')
    draw.ellipse((325,50,350,75), fill='white')

    # mouth
    draw.ellipse((250,130,350,140), fill='white')

    stick_figure.show()

# RUN IT!
# width = 500
# height = 500
draw_stick_figure()

print('    >> PROGRAM ENDED <<    ')