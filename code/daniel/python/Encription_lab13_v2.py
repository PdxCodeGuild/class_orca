'''
PDX Code Guild
Daniel Eggimann
Lab 13 Version 2
'''
# imports
import string

# generate list of characters to use in encryption
alphabet = string.ascii_lowercase
alpha_list = list(alphabet)

# gather user input for encryption
user_input = input('Enter a string of characters:  ')
user_encryption = int(input('Enter how many digits do you want to encrypt your string by:  '))

# convert string to list to facilitate manipulation of data
to_encrypt = list(user_input)
encrypted = []

# loop through user input to encrypt 
for letter in to_encrypt:
    if letter in alpha_list:
        # cross reference alphabet to gather index
        new_index = alpha_list.index(letter)
        # manipulate new index in accordance with encryption magnitude
        if new_index <= (25 - user_encryption): # determine point at which indices would exceed
            new_index += user_encryption        # range and subtract the encryption magnitude
            encrypted.append(alpha_list[new_index])
        elif new_index > (25 - user_encryption):
            new_index %= user_encryption
            encrypted.append(alpha_list[new_index])

# convert list back to string for reading comprehension
encrypted = ''.join(encrypted)

# output
print(encrypted)