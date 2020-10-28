##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab13-rot13.md
##############################################################################

# Have a dictionary or list of characters
english_characters = [
    'a',    'b',    'c',    'd',    'e',
    'f',    'g',    'h',    'i',    'j',
    'k',    'l',    'm',    'n',    'o',
    'p',    'q',    'r',    's',    't',
    'u',    'v',    'w',    'x',    'y',
    'z', # If changing length of list, remember to change modulus number below!
]


def encrypt(input, cipher_rotation_amount):
    
    # Welcome
    print('Welcome to Toddler Encrypt v1.0. Do not use for actual espionage!')

    user_output_encrypted = ''

    # Here's the actual 'encryption'
    # First we lookup every single character in the string...
    for character in user_input_modified:

        # If it's in our character list...
        if character in english_characters:
            
            # NOTE DICTIONARY WOULD USE: english_characters.get(character)
            # This example would 'encrypt' with the indexed english number, another great toddler version!
            # user_output_encrypted += str(english_characters.index(character)) + ' ' 

            
            
                # First we get the position of where to 'pick' the encrypted character
            output_character_index = 0
                # Lookup the index number of the character, so index(0) for an 'a'
                # Then add the cipher rotation amount
                # But don't forget to modulus that by 26 ### OR the number items in our list/dictionary
                # This is important so it loops around! So an 'a' with cipher of 26 will loop back around to become an 'a' again
            output_character_index = ( english_characters.index(character) + cipher_rotation_amount ) % 26

            # Above steps were numerical, now we'll looup the actual letter...
            output_character = english_characters[output_character_index]
            # ... and add it to our user_output_encrypted string
            user_output_encrypted += output_character

        # Otherwise, if the user's character is NOT in our list/dictionary lookup, append the exact character without any modification:
        else:
            user_output_encrypted += character

    # Return encrypted string
    print(f'Your input \"{user_input}\" should be encrypted as: \n\"{user_output_encrypted}\"\nGoodbye!')
    return user_output_encrypted



# Prompt user for input string
user_input = input('Please enter the message to encrypt: ')
# user_input = 'MAMA PC PC PC 0924jy g EErrrrrRRRR33*(&%' # TEMP non-input, predefined string for testing
user_input_modified = user_input.lower() # .lowercase() their string

# ASK USER HOW MUCH THE CIPHER SHOULD SHIFT
# cipher_rotation_amount = 1 # TEMP non-input, predefined string for testing
cipher_rotation_amount = input('Please enter the number of characters the cipher should shift, as a single number: ')
cipher_rotation_amount = int(cipher_rotation_amount)
# TODO add other input checking code here...


# Call it!
encrypt(user_input,cipher_rotation_amount)







# ***************************** WORKING FROM HERE *****************************
# ***************************** ^^^^^^^^^ TO HERE *****************************
##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab13-rot13.md
##############################################################################
# Lab 13: ROT Cipher

# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.
# Index 	0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20 	21 	22 	23 	24 	25
# English 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z
# ROT+13 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m
# Version 2 (optional)

# Allow the user to input the amount of rotation used in the encryption / decryption.