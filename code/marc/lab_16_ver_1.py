#This is version one of the image manipulation lab
# 1. First thing is to download pillow for python
# 2. Then you have to download the image (I will use the Lena image)
# 3. Then you have to manipulate the image to make it grayscale
#     -using this formula Y = 0.299*R + 0.587*G + 0.114*B
# 4. There is a code block given in the lab to shortcut the process

def main():
    from PIL import Image
    img = Image.open("Lenna_(test_image).png") # must be in same folder
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            Y = 0.299*r + 0.587*g + 0.114*b
            r = int(Y)
            g = int(Y)
            b = int(Y)

            # your code here

            pixels[i, j] = (r, g, b)

    img.show()
main()