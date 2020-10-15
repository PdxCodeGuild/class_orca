# imports image drawing stuff from pillow and gets randint from ranom
from PIL import Image, ImageDraw
from random import randint

# defines size of the image
width = 500
height = 500

# sets image to a name and sets the color set and dimensions
img = Image.new('RGB', (width, height))
# allows drawing to the image
draw = ImageDraw.Draw(img)

# creates 1000 random lines for background. color, start and end location, and width are all randomised
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

# sets the location and size of the head
circle_x = width/2
circle_y = height/5
circle_radius = 70
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

# draws body by starting at base of head and going down
draw.line((width/2 ,height/5+70, width/2, height/5+260), fill='black', width = 15)

# draws arms as a line a set distance from center of head
draw.line((width/2-120, height/5+130, width/2+120, height/5+130), fill='black', width= 15)

# draws legs as two lines going in different directions away from bottom of body
draw.line((width/2, height/5+260, width/2-120, height/5+350), fill='black', width=15)
draw.line((width/2, height/5+260, width/2+120, height/5+350), fill='black', width=15)

# shows the radical dude
img.show()