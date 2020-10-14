'''
Lab 22
Matthew Chimenti
'''

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

remove_words = ['The']
with open('gets.txt', 'r') as get_file:
    contents = get_file.read()

    words = contents.split(' ')
    word_count = len(words)
    letters = ''

    # sentence count
    words = ''.join(words)

    count = contents.count("!")
    count += contents.count("?")
    count += contents.count(":")
    count += contents.count(". . .")
    # print(count)
    # print(word_count)


    for i in words:
        if i not in [",", " ", "'", ";", "!", ".", "\n"]:
            letters += i
    characters = len(list(letters))


answer = 4.71 * (characters / word_count) + 0.5 * (word_count / count) - 21.43

rounded_answer = math.ceil(answer)

if rounded_answer in ari_scale:
    grade_level = ari_scale[rounded_answer]['grade_level']
    ages = ari_scale[rounded_answer]['ages']

    print(f'The ARI for gettysburg-address is {rounded_answer}')
    print(f'This corresponds to a {grade_level}')
    print(f'that is suitable for an average person {ages} years old')


