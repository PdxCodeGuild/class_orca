
# imports string to us to take whitespace out
import string

# opens an external file, sets its mode to read, and converts to utf8
with open('frankenstein.txt', 'r', encoding='utf8') as t:
    text = t.read()
    
    # dictionary of dictionaries with appropriate age and grade level for ARI
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
    # function that turns the text from the file into a list of individual characters without whitespace or punctuation
    def character():
        punct = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '—', '“', '”']
        char_split = [char for char in text if char not in string.whitespace]
        char_split = [char for char in char_split if char not in punct]
        return char_split

    # turns the text into a list of words
    word = text.split(' ')
    # turns the text into a list of sentences
    sentence = text.split('.')

    # counts the number of elements in each list and plugs it into a formula that will return a whole number that will be the ARI
    ari = (4.71 *(len(character()) / len(word)) + 0.5 * (len(word) / len(sentence)) - 21.43) // 1

    # prints the ARI and pulls the appropriate age and grade level from the dictionary
    print(f'The ARI for the first part of "Frankenstein; or, The Modern Prometheus" is {ari}.')
    print(f'This corresponds to a {ari_scale[ari]["grade_level"]} and should be suitable for an average person {ari_scale[ari]["ages"]} years old.')