# words = {'hello':2, 'how':8, 'are':1, 'you':6}
# check = list(words.items())
# # check = words.sort(lambda words.index(): words[1], reverse)
# print(check)
# check.sort(key= lambda check: check[1])
# print(check)

import math
with open('hello.txt') as all_text:
    text = all_text.read()
    #print(text)
 #putting all the uppers to lowers 
text2 = text.lower()
 #varibles
punctuation = '''!@#$%^&*?.,<>'''
no_punct = ''
 #this counts sentences 
sentences = float(text2.count('.'))
print (sentences, 'senten')
 #replaces punctuation with a space 
for char in text2:
    if char not in punctuation:
        no_punct = no_punct + char
       # print (no_punct)
#take out all spaces so you can count characters 
for space in no_punct:
    if space in no_punct:
        no_punct = no_punct.replace(' ','')
        #print (no_punct)
#gets the numer of characters 
characters = float(len(no_punct))
print (characters, 'chars')

words = text2.split(' ')
   # print(words)
 #this will give you how many words
num_words = float(len(words))
    #print ('number of words ',num_words)

ari = 4.71 *(characters / num_words) + 0.5 * (num_words / sentences) - 21.43
#round numbers up
ari_rounded = math.ceil(ari)
#print (ari_rounded)
# if it is over 14 this will catch it 
if ari_rounded >= 14:
    ari_rounded = 14

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
   

ages = (ari_scale[ari_rounded]['ages'])
grade = (ari_scale[ari_rounded]['grade_level'])
print (f'The Ari for this text is {ari_rounded}')
print (f'This is equivilent to a grade level of {grade} \nthat is normal for a person {ages} years old!')