from PIL import Image

def open_it():
    pic = input('Enter image name with extension in same directory or enter nothing for example picture: ')
    if pic == '':
        img = Image.open('Aybabtu.png') # must be in same folder
    else:
        img = Image.open(pic)
    return img
    
img = open_it()
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        Y = 0.299*r + 0.587*g + 0.114*b
        r = int(Y)
        g = int(Y)
        b = int(Y)

        pixels[i, j] = (r, g, b)

img.show()