# Welcome to lab22 by Quinton Baseman

#open the scratch file
with open('scratch.txt') as f:
    contents = f.read()
# how many words are in the file and store the number in the words variable
word = contents.split(' ')
words = len(word)


# the number of characters in the file
characters = 0
for i in word:
    for x in i:
        characters += 1
# the number of sentences in the file
sentence = contents.split('.')
sentences = len(sentence)
# dictionary of ages/grade level based on ari score
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
# equation to find out the final score
final_score = 4.71 * (characters/words) + .5 * (words/sentences) - 21.43
if final_score <= 13:
    final_score = round(final_score)
else:
    final_score = 14

# print final ouput
print(f'''

The ARI for this text is {final_score}
This corresponds to a {ari_scale[final_score]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[final_score]['ages']} years old.

''')

f.close()