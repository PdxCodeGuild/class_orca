from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

#body
draw.line((250, 200, 250, 400), fill='black', width=20)
#right leg
draw.line((250, 380, 300, 490), fill='black', width=20)
#left leg
draw.line((250, 380, 200, 490), fill='black', width=20)
#right arm
draw.line((250, 220, 310, 290), fill='black', width=20)
#left arm
draw.line((250, 220, 190, 290), fill='black', width=20)

#body
draw.line((400, 250, 400, 400), fill='black', width=15)
#right leg
draw.line((400, 400, 360, 490), fill='black', width=15)
#left leg
draw.line((400, 400, 440, 490), fill='black', width=15)
#right arm
draw.line((400, 290, 450, 360), fill='black', width=15)
#left arm
draw.line((400, 290, 350, 360), fill='black', width=15)

#body
draw.line((100, 250, 100, 400), fill='black', width=15)
#right leg
draw.line((100, 400, 60, 490), fill='black', width=15)
#left leg
draw.line((100, 400, 140, 490), fill='black', width=15)
#right arm
draw.line((100, 290, 150, 360), fill='black', width=15)
#left arm
draw.line((100, 290, 50, 360), fill='black', width=15)



circle_i = 100
circle_o = 250
circle_io_radius = 30
draw.ellipse((circle_i-circle_io_radius, circle_o-circle_io_radius, circle_i+circle_io_radius, circle_o+circle_io_radius), fill='black')


circle_a = 400
circle_b = 250
circle_ab_radius = 30
draw.ellipse((circle_a-circle_ab_radius, circle_b-circle_ab_radius, circle_a+circle_ab_radius, circle_b+circle_ab_radius), fill='black')


circle_x = width/2
circle_y = height/3.2
circle_radius = 45
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

img.show()