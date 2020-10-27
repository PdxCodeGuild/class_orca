from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)



draw.line((250, 250, 250, 270), fill="white")
draw.line((250, 270, 240, 280), fill="white")
draw.line((250, 270, 260, 280), fill="white")
draw.line((250, 260, 240, 250), fill="white")
draw.line((250, 260, 260, 250), fill="white")

circle_x = 250
circle_y = 245
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='white')

img.show()