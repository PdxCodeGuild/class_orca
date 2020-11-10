'''
PDX Code Guild
Daniel Eggimann
Lab16 Version 3
'''
from PIL import Image, ImageDraw

width = 1000
height = 1000

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


draw.rectangle(((0, 0), (width, height)), fill="white")

# draw.arc((25, 25), (75, 25), 0, 180, fill="black")

# stick figure head
circle_x = width/4
circle_y = height/4
circle_radius = 250
draw.ellipse((400, 75, 600, 275), outline='black')

# stick figure torso
draw.rectangle((465, 300, 535, 525), outline="black")

# stick figure arms
# left arm
draw.polygon((455, 300, 355, 525), outline="black")
# right arm
draw.polygon((545, 300, 645, 525), outline="black")

# stick figure legs
# left leg
draw.line((475, 535, 400, 835), fill='black')
# right leg
draw.line((525, 535, 600, 835), fill='black')


img.show()