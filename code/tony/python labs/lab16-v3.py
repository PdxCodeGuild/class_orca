from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0, 0), (width, height)), fill=(222,194,222))

draw.rectangle(((width/2-5, 150), (width/2+5, 350)), fill="black")
draw.line(((150, 240), (width/2, 255)), fill="black", width=3)
draw.line(((width/2, 256), (320, 175)), fill="black", width=2)
draw.line(((205,470), (width/2-5, 350)), fill=(29,36,118), width=7)
draw.line(((width/2+5,350), (300,470)), fill=(29,35,118), width=7)


circle_x = width/2
circle_y = 150
circle_radius = 44
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill=(0,113,124))

img.show()