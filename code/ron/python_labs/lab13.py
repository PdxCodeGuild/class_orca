

# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
# Assignment/Ver: Lab13
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-09-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 
Lab 13: ROT Cipher
'''
#----Modules------------------------------------------------

import math
import string
import random

#----Global variables, lists, dictionaries------------------

''' None '''

#----Functions----------------------------------------------

''' None '''

#--------Main Code------------------------------------------

def main():

    # Input 
    print('\n  *** Encryption/Decryption ***')
    user_input = input('\nPlease enter string: ')
    user_rotation = input('Rotation: ')
    rotation = int(user_rotation)

    # Break string into list
    user_input = list(user_input)

    # Convert list into ascii values
    user_input = [ord(user_input[x]) for x in range(len(user_input))]

    # Encryption
    user_input = [(user_input[x] + rotation) 
        if user_input[x] < 109
        else user_input[x] - rotation
        for x 
        in range(len(user_input))
        ]

    # Decryption
    user_input = [chr(user_input[x]) for x in range(len(user_input))]

    # Output
    output = "".join(user_input)
    output = output.replace('-', ' ')
    print(f'\nEncrypted/Decrpyted: {output}\n')

main()

#--------End Code-------------------------------------------
