import string
import math
from nltk import tokenize

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

with open('580-0.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

characters_list = list(contents)
characters = []
for i in characters_list:
    if i in string.ascii_letters or i in string.digits:
        characters.append(i)

words = contents.split()

sentences = tokenize.sent_tokenize(contents)

ARI = (4.71 * len(characters) / len(words)) + (0.5 * len(words) / len(sentences)) - 21.43


print(f'The ARI for "The Pickwick Papers", by Charles Dickens is {math.ceil(ARI)}')

ARI_grade = ari_scale[math.ceil(ARI)]['grade_level']
ARI_age = ari_scale[math.ceil(ARI)]['ages']
print(f'This corresponds to a(n) {ARI_grade} level of difficulty"\n"that is suitable for an average person {ARI_age} years old')

