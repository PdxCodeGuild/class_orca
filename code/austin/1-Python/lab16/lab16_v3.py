#Lab16 version 3: Draw a Stick Figure

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height), (255, 255, 255))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.line(((150, 285), (250, 151), (350, 285)), fill="yellow", width=3)
draw.line(((150, 285), (350, 285)), fill="yellow", width=3)

#body
draw.line([(250, 285), (250, 151)], fill="yellow", width=3)
draw.line([(175, 285), (175, 250)], fill="yellow", width=3)
draw.line([(325, 285), (325, 250)], fill="yellow", width=3)
draw.line([(212, 285), (212, 199)], fill="yellow", width=3)
draw.line([(288, 285), (288, 199)], fill="yellow", width=3)

#legs
draw.line([(270, 350), (270, 285)], fill="black", width=2)
draw.line([(230, 350), (230, 285)], fill="black", width=2)

#arms
draw.line([(212, 199), (160, 150)], fill="black", width=2)
draw.line([(288, 199), (337, 150)], fill="black", width=2)




circle_x = width/2
circle_y = 110
circle_radius = 40
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), outline="black", width=2)


img.show()