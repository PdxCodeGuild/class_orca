from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner
draw.rectangle(((0, 0), (width, height)), fill="white")



#body
draw.line(((250, 250), (250, 100)), fill='black', width=0)
#legs
draw.line(((200, 350), (250, 250)), fill='black', width=0)
draw.line(((300, 350), (250, 250)), fill='black', width=0)
#arms
draw.line(((175, 150), (250, 200)), fill='black', width=0)
draw.line(((325, 150), (250, 200)), fill='black', width=0)



#head
circle_x = width/2
circle_y = height/5
circle_radius = 30
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

img.show()