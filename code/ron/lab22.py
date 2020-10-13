
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab22
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-12-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 22: Compute ARI

'''
#----Modules------------------------------------------------

import math
import string
import io

#----Global variables, lists, dictionaries------------------

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

text_f = "getty.txt"

#----Functions----------------------------------------------

def strip(contents):
    '''Strip punctuation from raw contents '''
    translator = str.maketrans('', '', string.punctuation)
    new_chars = contents.translate(translator)
    return new_chars

def del_function(str_input):
    '''Delete any spaces or sentance breaks in text '''
    for x in range(len(str_input)):
        for i in str_input:
            if i in (" ", "\n"):
                str_input.remove(i)
    return str_input

        
#--------Main Code---------------------------------------------

def main(): 

    # Open file for reading
    with open(text_f) as f:
        contents = f.read()

    # Split text into word list and count
    new_contents = contents.split()
    word_count = len(new_contents)

    # Strip punctuation from raw contents
    new_chars = strip(contents)

    # Make list of 'characters' with no punctuation and then counts them
    characters = list(new_chars)

    characters = del_function(characters)

    # Count all the characters (no spaces or punctation)
    char_count = len(characters)

    # Count sentances in raw text based on number of periods '.' 
    sentance_count = contents.count('.')

    # ARI calculation rounded up
    ARI = math.ceil((4.71*(char_count/word_count)) + (.5 * (word_count/sentance_count) - 21.43))

    # Loop though dictionary and find ARI associated values
    for ari_key, info in ari_scale.items():
        if ari_key == ARI:
            age_level = (info['ages'])
            grade_level = (info['grade_level'])

    # Output and print results
    print(f'''
    ***** ARI Calculator *****

    No. of sentances: {sentance_count}
    No. of characters: {char_count}
    No. of words: {word_count}
    ARI: {ARI}

    The ARI for the "{text_f}" is {ARI}!  
    This corresponds to a(n) {grade_level} level of difficulty
    that is suitable for an average person {age_level} years old.
    ''')

main()