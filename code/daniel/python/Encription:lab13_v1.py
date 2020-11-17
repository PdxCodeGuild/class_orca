'''
PDX Code Guild
Daniel Eggimann
Lab 13 Version 1
'''
# imports
import string

# generate list of characters to use in encryption
alphabet = string.ascii_lowercase
alpha_list = list(alphabet)

# gather user input for encryption
user_input = input('Enter a string of characters:  ')

# convert string to list to facilitate manipulation of data
to_encrypt = list(user_input)
encrypted = []

# loop through user input to encrypt 
for letter in to_encrypt:
    if letter in alpha_list:
        # cross reference alphabet to gather index
        new_index = alpha_list.index(letter)
        # manipulate new index in accordance with encryption magnitude
        if new_index <= 12:
            new_index += 13
            encrypted.append(alpha_list[new_index])
        elif new_index >12:
            new_index %= 13
            encrypted.append(alpha_list[new_index])
    else:
        encrypted.append(letter)
# convert list back to string for reading comprehension
encrypted = ''.join(encrypted)

# output
print(encrypted)