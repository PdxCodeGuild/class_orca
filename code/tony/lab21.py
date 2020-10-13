# todo
# Version 3:
# let the user enter a word then show the words which most frequently follow

# ---------------------
import time
import string
import stopwords
book_dict = {}
stop = stopwords.stopper()

# open book file
soap = 'soap.txt'
book = open(file=soap, mode='r', encoding='UTF-8').read()

print(f'\nOpened file {soap}. May take a bit to return results.\n')
time.sleep(.5)

# lowercase all letters in file
book_lower = book.lower()

# function to strip file of punctuation
def punc_stripper(to_strip):
    punct_stripper = to_strip.translate(str.maketrans('','',string.punctuation))
    return punct_stripper

# run lowercase file through function and split file into words.
stripped_book = punc_stripper(book_lower)
book_split = stripped_book.split()

print('Adding words and count to dictionary...')
time.sleep(.5)
# add words in file list and word frequency into dictionary.
for x in book_split:
    if x in book_dict:
        book_dict[x] += 1
    else:
        book_dict[x] = 1

print('Removing common words...')
time.sleep(.5)
# removes words in stopwords list (imported stopwords.py in same directory)
for x in stop:
    if x in book_dict:
        book_dict.pop(x)

print('Arranging order of words...')
time.sleep(.5)
# sorting counted list of words in descending order and then printing results
words = list(book_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)

print('\nTop 10 words in this book are: \n')

for i in range(min(10, len(words))):
    print(words[i])