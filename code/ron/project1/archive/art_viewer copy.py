
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Capstone 1.0
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-27-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 
Capstone 1.0 - Art Viewer
 
'''
#----Modules--------------------------------------------------------

import art_mod

from PIL import ImageTk, Image
import tkinter as tk
import PIL
import re
import os

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

def fwd(img_num):
    global button_back
    global button_fwd
    global art_image

    art_image.grid_forget()
    art_image = tk.Label(canvas_1, image = img[img_num - 1])
    button_fwd = tk.Button(window_1_frame, text = ">>", command = lambda: fwd(img_num + 1))
    button_back = tk.Button(window_1_frame, text = "<<", command = lambda: back(img_num - 1))
    
    if img_num == len(current_artist):
        button_fwd = tk.Button(window_1_frame, text = ">>", state = tk.DISABLED)
    
    art_image.grid(column = 0, row = 0, padx = 0, pady = 0)
    button_back.grid(column = 0, row = 1, padx = 10, pady = 10)
    button_fwd.grid(column = 1, row = 1, padx = 10, pady = 10)

def back(img_num):
    global button_back
    global button_fwd
    global art_image

    art_image.grid_forget()
    art_image = tk.Label(canvas_1, image = img[img_num - 1])
    button_fwd = tk.Button(window_1_frame, text = ">>", command = lambda: fwd(img_num + 1))
    button_back = tk.Button(window_1_frame, text = "<<", command = lambda: back(img_num - 1))
    
    if img_num == 1:
        button_back = tk.Button(window_1_frame, text = "<<", state = tk.DISABLED)
    
    art_image.grid(column = 0, row = 0, padx = 0, pady = 0)
    button_back.grid(column = 0, row = 1, padx = 10, pady = 10)
    button_fwd.grid(column = 1, row = 1, padx = 10, pady = 10)

def change_artist(new_artist):
    global current_artist
    global img
    global art_image

    art_image.grid_forget()
    current_artist = []
    img = []
    current_artist = build_list(new_artist)
    for y in current_artist:
        img.append(ImageTk.PhotoImage(Image.open(f"data/art_images_copy/" + y)))
        #^ Creates list of new images for current artist selected
    art_image = tk.Label(canvas_1, image = img[0])
    art_image.grid(column = 0, row = 0, padx = 0, pady = 0)

def import_data():

    # Open .csv file
    with open('./data/artists_test_data.csv', 'r') as file:
        lines = file.read().split('\n')

    # Breakout keys into unique list and delete from .csv
    keys = lines[0].split(',')
    del lines[0]

    # Populate contact list with user dicts
    for x in range(len(lines)):
        info = {}
        # Build temp list to hold user data
        temp = lines[x].split(',')
        # Take temp data and build dict
        for y in range(len(temp)):
            info[keys[y]] = temp[y]
        # Drop user dict into contacts list
        artists_data.append(info)
        print(artists_data)

def import_data():
    global artist_data

    # Open .csv file
    with open('./data/artists_test_data.csv', 'r') as file:
        lines = file.read().split('\n')
    # Breakout keys into unique list and delete from .csv
    keys = lines[0].split(',')
    del lines[0]

    artist_data = []    

    for x in range(len(lines)):
        info = {}
        new = []
        temp = lines[x].split(',')
        for z in range(5):
            new.append(temp[z])
            info[keys[z]] = new[z]
        # print(info, sep = '/n')
        artist_data.append(info)

def import_data():
    global artist_data

    # Open .csv file
    with open('./data/artists_test_data.csv', 'r') as file:
        lines = file.read().split('\n')
    # Breakout keys into unique list and delete from .csv
    keys = lines[0].split(',')
    del lines[0]

    artist_data = []    

    for x in range(len(lines)):
        info = {}
        new = []
        temp = lines[x].split(',')
        for z in range(5):
            new.append(temp[z])
            info[keys[z]] = new[z]
        # print(info, sep = '/n')
        artist_data.append(info)

def last_name_list():
    global last_name
    name = []
    last_name = []

    for x in artist_data:
        l = x['name'].split()
        name.append(l)
    for x in name:
        last_name.append(x[-1])
    return last_name

#----Main-----------------------------------------------------------

# Initialize window
root = tk.Tk()
# root.geometry('475x475')
root.resizable(1,1)
# root.iconbitmap('Put in the filename')

import_data()

img = []
options = last_name_list()
artist =  tk.StringVar()
artist.set(options[0])

current_artist = build_list(artist.get())
#^ Current artist is a list of selected artist's images/filenames

for y in current_artist:
    img.append(ImageTk.PhotoImage(Image.open(f"data/art_images_copy/" + y)))
    #^ Creates list of images for current artist selected

''' Root Information ----------------------------------------------------------'''
root.title("Who's Who in the 'Art World' Zoo")
title = tk.Label(root, text = art_mod.welcome_msg, bg = "gray", width = 100)

# Root placement
title.grid(column = 0, row = 0, columnspan = 2, padx = 5, pady = 5)

''' Window 1 - image and navigation buttons ----------------------------------'''
window_1_frame = tk.LabelFrame(root, height = 300, width = 200, text = "Artist Images")
canvas_1 = tk.Canvas(window_1_frame, height = 250, width = 190, bd = 1, bg = "grey", relief = "groove")
art_image = tk.Label(canvas_1, image = img[0])
    #^ Image initialization
button_back = tk.Button(window_1_frame, text = "<<", state = tk.DISABLED)
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
artist_name = tk.OptionMenu(window_2_frame, artist, *options)
artist_type = tk.Label(window_2_frame, width = 20, height = 5, text = "Label 2", bd = 1, relief = "sunken")
artist_info = tk.Label(window_2_frame, width = 20, height = 5, text = "Label 3", bd = 1, relief = "sunken")
button_update = tk.Button(window_2_frame, text = "Update", command = lambda: change_artist(artist.get()))
button_exit = tk.Button(window_2_frame, text = "Exit", command = root.quit)

# Window 2 placement
window_2_frame.grid(column = 1, row = 1, padx = 10, pady = 10)
    #^ Framework for window (1 col, 3 rows)
artist_name.grid(column = 1, row = 0, padx = 10, pady = 2)
button_update.grid(column = 1, row = 1, padx = 10, pady = 10)
artist_type.grid(column = 1, row = 2, padx = 10, pady = 10)
artist_info.grid(column = 1, row = 3, padx = 10, pady = 10)
button_exit.grid(column = 1, row = 4, padx = 5, pady = 5)


root.mainloop()


#----End-----------------------------------------------------------
