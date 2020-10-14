from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((240, 150), (260, 380)), fill="black")

# draw a line from x0, y0, x1, y1
# using the color pink
#right leg
draw.line((250, 380, 300, 490), fill='black', width=20)
#left leg
draw.line((250, 380, 200, 490), fill='black', width=20)
#right arm
draw.line((250, 220, 310, 290), fill='black', width=20)
#left arm
draw.line((250, 220, 190, 290), fill='black', width=20)



circle_x = width/2
circle_y = height/3.2
circle_radius = 45
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

img.show()