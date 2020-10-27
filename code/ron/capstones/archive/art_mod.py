
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Project_1.0
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-27-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 
Project_1.0 - Art

Modules
 
'''
#----Modules--------------------------------------------------------

from PIL import ImageTk, Image
import tkinter as tk
import PIL
import re
import os


#----Dictionary/Lists-------------------------------------------------

# class Art_viewer:
#    def __init__(self, artist):
#       self.artist = artist    


#----Classes--------------------------------------------------------





#----Global variables, lists, dictionaries--------------------------



# # Initialize window
# root = tk.Tk()
# # root.geometry('475x475')
# root.resizable(1,1)
# # root.iconbitmap('Put in the filename')

# welcome_msg = "Welcome!\nPlease select an Artist from the drop down menu,\n and scroll through the master's art!"

# img1 = ImageTk.PhotoImage(Image.open("data/art_images/Albrecht_Dürer_17.jpg"))



# # img2 = tk.ImageTk.PhotoImage(Image.open("data/art_images/Albrecht_Dürer_7.jpg"))
# # img3 = tk.ImageTk.PhotoImage(Image.open("data/art_images/Albrecht_Dürer_27.jpg"))
# # img4 = tk.ImageTk.PhotoImage(Image.open("data/art_images/Albrecht_Dürer_57.jpg"))
# # img5 = tk.ImageTk.PhotoImage(Image.open("data/art_images/Albrecht_Dürer_77.jpg"))

# image_list = [img1]

# # img2, img3, img4, img5]


# #----Functions------------------------------------------------------

# print(image_list)

# root.mainloop()

#----Main-----------------------------------------------------------

# artists = ["Vincent_Van Gogh_123.jpg", "some other fuck", "Vincent_Van Gogh_125.jpg","Vincent_Van Gogh_126.jpg","Vincent_Van Gogh_127.jpg", "some fuck"]

name = "Monet"

dir_list = os.listdir('./data/art_images_copy')
artists = list(dir_list)
current_artist = []

for artist in artists:
    if re.search('.+_'+ name + '_.+', artist):
        current_artist.append(artist)
print(current_artist)
    # else:
    #     print(False)



# print(dir_list)

