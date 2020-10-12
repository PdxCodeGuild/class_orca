import string

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



with open('pearl_harbor_address.txt', encoding = 'utf-8') as speech:
    contents = speech.read()

words = contents.split(' ')
words_count = len(words)

chars = string.ascii_letters
chars_list = list(contents)
char = []

for i in chars_list:
    if i in chars:
        char.append(i)

total_chars = len(char)

sentences = contents.split('.')
sentence_count = len(sentences)


# print(words_count)
# print(sentence_count)
# print(total_chars)
# # print(contents)

ari = 4.71 * (float(total_chars) / float(words_count)) + (0.5 (float(words_count) / float(sentence_count))) - 21.43)

print(ari)
