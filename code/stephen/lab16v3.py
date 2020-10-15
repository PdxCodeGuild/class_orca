from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0, 0), (width, height)), fill = "cyan")

circle_radius1 = 60
circle_radius2 = 50
circle_radius3 = 10
draw.ellipse((250-circle_radius1, 100-circle_radius1, 250+circle_radius1, 100+circle_radius1), fill='black')
draw.ellipse((250-circle_radius2, 100-circle_radius2, 250+circle_radius2, 100+circle_radius2), fill='white')
draw.ellipse((230-circle_radius3, 90-circle_radius3, 230+circle_radius3, 90+circle_radius3), fill='black')
draw.ellipse((270-circle_radius3, 90-circle_radius3, 270+circle_radius3, 90+circle_radius3), fill='black')
draw.line((150, 205, 350, 205), fill=('black'), width=10)
draw.line((250, 350, 250, 150), fill=('black'), width=10)
draw.line((150, 480, 250, 350), fill=('black'), width=10)
draw.line((350, 480, 250, 350), fill=('black'), width=10)
draw.chord((235, 100, 265, 120), start=0, end=180, fill=('black'))

img.show()