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



# making function to determine number of total words
def words_count(total_words):
    words = contents.split(' ')
    total_words = len(words)
    return total_words

# making function to determine number of characters that are present in ascii.letters
def character_count(context):
    chars = string.ascii_letters
    chars_list = list(contents)
    char = []

    for i in chars_list:
        if i in chars:
            char.append(i)

    total_chars = len(char)
    return total_chars

# making function to find total number of sentences by splittings at each .
def sentence_count(total_sentences):
    sentences = contents.replace('?', '.')
    sentences = contents.replace('!', '.')
    sentences = contents.split('.')
    total_sentences = len(sentences)
    return total_sentences

# making function to compute the ARI formula 
def ari_total(total_chars, total_sentences, total_words):

    ari = 4.71 * (float(chars) / float(words)) + (0.5 * (float(words) / (float(sentences))) - 21.43)
    return ari

# opening text file
with open('pearl_harbor_address.txt', encoding = 'utf-8') as speech:
    contents = speech.read()

# setting variables to run functions
chars = character_count(contents)
sentences = sentence_count(contents)
words = words_count(contents)

# using math module to perform ceiling division and get final score
score = math.ceil(ari_total(chars, words, sentences))
if score > 14:
    score == 14

# setting variable to get age from dictionary to pass into f-string
age_level = ari_scale[score]
grade_level = ari_scale[score]
# just getting the value at ages
age = age_level['ages']
grade = grade_level['grade_level']

print(f'The Pearl Harbor Address has an ARI score of {score}.\nThis is a reading level for {grade} and is suitable for people aged {age}.')

# print(sentences)

