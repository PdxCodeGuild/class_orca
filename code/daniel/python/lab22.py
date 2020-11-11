# imports
import math


def active_file():
    '''call .txt file for manipulation'''
    with open('civil_disobediance.txt', 'r') as f:
        contents = f.read()
        return contents

def character_count(contents):
    '''determine character count by replacing ' ' with '' and taking len(str)'''
    character_count = contents.replace(' ', '')
    return len(character_count)

def word_count(contents):
    '''determine word count by converting file to a list of strings'''
    content_list = contents.split()
    word_count = len(content_list)
    return word_count

def sentence_count(contents):
    '''determine number of sentences by replacing "!" and "?" with "."'''
    sentence_count = contents.replace('?', '.')
    sentence_count = contents.replace('!', '.')
    sentence_count = contents.split('.')
    return len(sentence_count)

def ari(characters, words, sentences):
    ari = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
    ari = math.ceil(ari)
    return ari

def grade_level(ari):
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
    for key in ari_scale:
        if ari == key:
            return ari_scale[key]['ages'], ari_scale[key]['grade_level']
    


def main():
    contents = active_file()
    characters = character_count(contents)
    words = word_count(contents)
    sentences = sentence_count(contents)
    ARI = ari(characters, words, sentences)
    age, grade = grade_level(ARI)

    print(f'''The ARI for Civil Disobediance is {ARI}.
This corresponds to a {grade} level of difficulty 
that is suitable for an average person {age} years old.
    '''
    )

main()
