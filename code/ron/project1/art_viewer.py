
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
    ''' Returns file names for 'current artist' based on artist selected '''
    dir_list = os.listdir('./data/art_images_copy')
    artists = list(dir_list)
    current_artist = []
    for artist in artists:
        if re.search('.+_'+ name + '_.+', artist):
            #^ Searhes for last name regardless of other characters
            current_artist.append(artist)
    return current_artist

def fwd(img_num):
    ''' Forward Button functionality '''
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
    ''' Back Button functionality '''

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
    ''' Updates artist information, images, and labels '''
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
    refesh_labels(new_artist)

def import_data():
    ''' Imports and scrubs data for artist_data list '''
    global artist_data

    # Open .csv file
    with open('./data/artists_test_data.csv', 'r') as file:
        lines = file.read().split('\n')
    # Breakout keys into unique list and delete from .csv
    keys = lines[0].split(',')
    del lines[0]

    artist_data = []    

    # Splits data into temp list, reconfigures data, builds artist list of dicts 
    for x in range(len(lines)):
        info = {}
        new = []
        temp = lines[x].split(',')
        for z in range(5):
            new.append(temp[z])
            info[keys[z]] = new[z]
        artist_data.append(info)

def last_name_list():
    ''' Returns list of only last times for combo box '''
    global last_name
    name = []
    last_name = []

    for x in artist_data:
        l = x['name'].split()
        name.append(l)
    for x in name:
        last_name.append(x[-1])
    #^ reverses name order and creates new list
    return last_name

#----Main-----------------------------------------------------------

# Initialize GUI
root = tk.Tk()
root.resizable(1,1)

''' Initialize program state and declare variables -----------------------'''
import_data()
img = []
options = last_name_list()
artist =  tk.StringVar()
artist.set(options[0])
genre = ""
nation = ""
current_artist = build_list(artist.get())
#^ Current artist is a list of selected artist's images/filenames
for y in current_artist:
    img.append(ImageTk.PhotoImage(Image.open(f"data/art_images_copy/" + y)))
    #^ Creates list of images for current artist selected

''' Root Information ----------------------------------------------------------'''
root.title("Who's Who in the 'Art World' Zoo")
title = tk.Label(root, text = art_mod.welcome_msg, bg = "#ADAD85", width = 100)

# Root placement
title.grid(column = 0, row = 0, columnspan = 2, padx = 5, pady = 5)

''' Window 1 - image and navigation buttons ----------------------------------'''
window_1_frame = tk.LabelFrame(root, height = 300, width = 200, text = "Artist Images")
canvas_1 = tk.Canvas(window_1_frame, height = 250, width = 190, bd = 1, bg = "grey", relief = "groove")
art_image = tk.Label(canvas_1, image = img[0])
    #^ Image box
button_back = tk.Button(window_1_frame, text = "<<", state = tk.DISABLED)
button_fwd = tk.Button(window_1_frame, text = ">>", command = lambda: fwd(2))

# Window 1 placement
window_1_frame.grid(column = 0, row = 1, padx = 18, pady = 10)
    #^ Framework for window (1 col, 2 rows)
canvas_1.grid(column = 0, row = 0, columnspan = 2, padx = 10, pady = 10)
button_back.grid(column = 0, row = 1, padx = 10, pady = 10)
button_fwd.grid(column = 1, row = 1, padx = 10, pady = 10)
art_image.grid(column = 0, row = 0, padx = 0, pady = 0)

''' Window 2 (information) - artist selection and associated info ---------------'''
window_2_frame = tk.LabelFrame(root, height = 300, width = 200, text = "Artist Information", bg = "#ADAD85")
artist_name = tk.OptionMenu(window_2_frame, artist, *options)
artist_genre_label = tk.Label(window_2_frame, width = 20, height = 1, text = "Artist Genre", bg = "#ADAD85")
artist_genre = tk.Label(window_2_frame, width = 20, height = 1, text = genre, bd = 1, relief = "sunken")
artist_nationality_label = tk.Label(window_2_frame, width = 20, height = 1, text = "Artist Nationality", bg = "#ADAD85")
artist_nationality = tk.Label(window_2_frame, width = 20, height = 1, text = nation, bd = 1, relief = "sunken")
button_update = tk.Button(window_2_frame, text = "Update", command = lambda: change_artist(artist.get()))
button_exit = tk.Button(window_2_frame, text = "Exit", command = root.quit)

# Window 2 placement
window_2_frame.grid(column = 1, row = 1, padx = 5, pady = 5)
    #^ Framework for window (1 col, 7 rows)
artist_name.grid(column = 1, row = 0, padx = 5, pady = 5)
button_update.grid(column = 1, row = 1, padx = 5, pady = 5)
artist_genre_label.grid(column = 1, row = 2, padx = 5, pady = 0)
artist_genre.grid(column = 1, row = 3, padx = 5, pady = 5)
artist_nationality_label.grid(column = 1, row = 4, padx = 5, pady = 2)
artist_nationality.grid(column = 1, row = 5, padx = 5, pady = 2)
button_exit.grid(column = 1, row = 6, padx = 6, pady = 20)

def refesh_labels(artist):
    ''' Refreshes artist nationality, genre data when artist selected '''
    global artist_genre
    global artist_nationality

    print(artist)
    for y in artist_data:
        for key, value in y.items():
            if artist in value:
                artist_genre = tk.Label(window_2_frame, width = 20, height = 1, text = y['genre'], bd = 1, relief = "sunken")
                artist_nationality = tk.Label(window_2_frame, width = 20, height = 1, text = y['nationality'], bd = 1, relief = "sunken")
                    
    artist_genre.grid(column = 1, row = 3, padx = 5, pady = 5)
    artist_nationality.grid(column = 1, row = 5, padx = 5, pady = 2)
    #^ Reintializes labels with new values

refesh_labels(artist.get())

root.mainloop()


#----End-----------------------------------------------------------
