from PIL import Image
import colorsys

# functions --------------------------------------

# opens user file or example file, returns error message and loop if invalid file/location
# default image is: aybabtu.png
def open_it():
    pic = input('Enter image name with extension or enter nothing for example picture: ')
    if pic == '':
        img = Image.open('Aybabtu.png')
    elif pic == 'exit':
        exit()
    else:
        try:
            img = Image.open(pic)
        except:
            print('Could not find image!\n')
            return open_it()
    return img

# edits image via HSV values    
def HSV(x,y,z):
    h, s, v = colorsys.rgb_to_hsv(x/255, y/255, z/255)
    h = h* 6
    s = s* 0.5
    v = v* 1.6

    x, y, z = colorsys.hsv_to_rgb(h, s, v)
    
    x = int(x*255)
    y = int(y*255)
    z = int(z*255)
    return x,y,z

#------------------------------------------------

img = open_it()
width, height = img.size
pixels = img.load()
choice = ''


# if choice is not among options, loop
while choice != 'hsv' and choice != 'monochrome' and choice != 'exit':
    choice = input('HSV, Monochrome, or Exit? ').lower()

# runs HSV edit and shows image
if choice == 'hsv':
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r, g, b = HSV(r,g,b)

            pixels[i, j] = (r, g, b)
    img.show()

# edits image to be monochrome and shows image
elif choice == 'monochrome':
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            Y = 0.299*r + 0.587*g + 0.114*b
            r = int(Y)
            g = int(Y)
            b = int(Y)

            pixels[i, j] = (r, g, b)
    img.show()

# exit ofc
else:
    exit()