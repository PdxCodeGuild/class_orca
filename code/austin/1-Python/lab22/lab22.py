#Lab 22: Get ARI

import string
import math

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

def ari():
    with open('./dickens.txt', 'r') as text_file:
        contents = text_file.read()
        print(contents)
    
    sentence_count = contents.count('.')
    print(sentence_count, "sentence count")

    translator = str.maketrans('', '', string.punctuation)
    clean_text = contents.translate(translator)
    clean_text = clean_text.replace('\n', ' ')
    print(clean_text)

    #Get number of chars and words
    word_list = clean_text.split(" ")
    print(word_list)

    char_list = list(clean_text)
    # print(char_list)

    word_count = len(word_list)

    char_count = len(char_list)
    
    print(word_count)
    print(char_count)

    #Get ARI calculation
    raw_ari = math.ceil(((4.71 * (char_count/word_count)) +  (0.5 * word_count/sentence_count)) - 21.43) 
    print(raw_ari)

    #Compare to ARI scale
    if raw_ari in ari_scale:
        grade_level = ari_scale[raw_ari]['grade_level']
        age_range = ari_scale[raw_ari]['ages']
    
    if raw_ari >= 14:
        grade_level = ari_scale[14]['grade_level']
        age_range = ari_scale[14]['ages']
    

    print(f'The ARI for an excerpt from Great Expectations is {raw_ari} \n This corresponds to a {grade_level} grade level, or one suitable for readers {age_range} years old')

ari()


    
