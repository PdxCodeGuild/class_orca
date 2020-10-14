# this is version 3 of the image manipulation lab. It involves drawing a stick figure.

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")
#this is basically creating a blank canvas to draw on

# draw a rectangle from x0, y0 to x1, y1
# draw.rectangle(((100, 100), (300, 300)), fill="green")

# draw a line from x0, y0, x1, y1
# using the color pink
# color = (256, 128, 128)  # pink
draw.line((width - 325, (height - 375), width - 175, (height - 375)), fill="black")#shoulders
draw.line((width - 325, (height - 375), width - 325, (height - 250)), fill="black")#right arm
draw.line((width - 175, (height - 375), width - 175, (height - 250)), fill="black")#left arm
draw.line((width/2, (height - 450), width/2, (height - 250)), fill= "black") #body
draw.line((width/2, (height - 250), (width - 225), (height )), fill= "black")#right leg
draw.line((width/2, (height - 250), (width - 275), (height )), fill= "black")#left leg


circle_x = width/2
circle_y = height - 450
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

img.show()