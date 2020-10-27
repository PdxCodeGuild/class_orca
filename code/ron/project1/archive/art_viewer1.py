
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Project_1.0
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-27-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 
Project_1.0 - Art Viewer
 
'''
#----Modules--------------------------------------------------------

# import art_mod

from PIL import ImageTk, Image
import tkinter as tk
import PIL
import re
import os

#----Dictionary/Lists-------------------------------------------------



#----Global variables, lists, dictionaries--------------------------



#----Functions------------------------------------------------------

def build_list(name):
    
    dir_list = os.listdir('./data/art_images_copy')
    artists = list(dir_list)
    current_artist = []

    for artist in artists:
        if re.search('.+_'+ name + '_.+', artist):
            current_artist.append(artist)
    
    return current_artist

# def button_fwd(current_artist, img_num):
#     global button_back
#     global button_fwd
#     global art_image

#     art_image.grid_forget()
#     art_image = tk.Label(canvas_1, image = current_artist[img_num -1])
#     art_image.grid(column = 0, row = 0, padx = 0, pady = 0)



#----Main-----------------------------------------------------------


# Initialize window
root = tk.Tk()
# root.geometry('475x475')
root.resizable(1,1)
# root.iconbitmap('Put in the filename')

current_artist = build_list("Monet")

img = []

for y in current_artist:
    img.append(ImageTk.PhotoImage(Image.open(f"data/art_images_copy/" + y).resize(300, 300)))


''' Root Information -------------------------------------------------'''
root.title("Who's Who in the 'Art World' Zoo")
title = tk.Label(root, text = "test", underline = 100)
button_exit = tk.Button(root, text = "Exit", command = root.quit)

# Root placement
title.grid(column = 0, row = 0, columnspan = 2, padx = 5, pady = 5)
button_exit.grid(column = 0, row = 2, columnspan = 2, padx = 5, pady = 5)

''' Window 1 (images) - image and navigation buttons -------------------'''
window_1_frame = tk.LabelFrame(root, height = 300, width = 200, text = "Artist Images")
canvas_1 = tk.Canvas(window_1_frame, height = 250, width = 190, bd = 1, bg = "grey", relief = "groove")
art_image = tk.Label(canvas_1, image = img[0])
    #^ Image initialization

def fwd(img_num):
    global button_back
    global button_fwd
    global art_image

    art_image.grid_forget()
    art_image = tk.Label(canvas_1, image = img[img_num - 1])
    art_image.grid(column = 0, row = 0, padx = 0, pady = 0)

def back():
    global button_back
    global button_fwd
    global art_image

    art_image.grid_forget()
    art_image = tk.Label(canvas_1, image = current_artist[img_num + 1])
    art_image.grid(column = 0, row = 0, padx = 0, pady = 0)

button_back = tk.Button(window_1_frame, text = "<<", command = back)
button_fwd = tk.Button(window_1_frame, text = ">>", command = lambda: fwd(2))

# Window 1 placement
window_1_frame.grid(column = 0, row = 1, padx = 18, pady = 10)
    #^ Framework for window (1 col, 3 rows)
canvas_1.grid(column = 0, row = 0, columnspan = 2, padx = 10, pady = 10)
button_back.grid(column = 0, row = 1, padx = 10, pady = 10)
button_fwd.grid(column = 1, row = 1, padx = 10, pady = 10)
art_image.grid(column = 0, row = 0, padx = 0, pady = 0)

''' Window 2 (information) - artist selection and associated info ---------------'''
window_2_frame = tk.LabelFrame(root, height = 300, width = 200, text = "Artist Information")
artist_name = tk.Listbox(window_2_frame, width = 20, height = 5, bd = 1, relief = "sunken", selectmode = "single")
artist_type = tk.Label(window_2_frame, width = 20, height = 5, text = "Label 2", bd = 1, relief = "sunken")
artist_info = tk.Label(window_2_frame, width = 20, height = 5, text = "Label 3", bd = 1, relief = "sunken")

# Window 2 placement
window_2_frame.grid(column = 1, row = 1, padx = 10, pady = 10)
    # Framework for window (1 col, 3 rows)
artist_name.grid(column = 1, row = 0, padx = 10, pady = 10)
artist_type.grid(column = 1, row = 1, padx = 10, pady = 10)
artist_info.grid(column = 1, row = 2, padx = 10, pady = 10)


    


ht = 200
wh = 300

root.mainloop()


#----End-----------------------------------------------------------
