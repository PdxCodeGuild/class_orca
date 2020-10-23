#Anki Automated Flashcard Maker

import nltk

# alphabet = "aбвгдеёжзийклмнопрстуфхцчшщъыьэюя"
nltk.download("stopwords")

from nltk.corpus import stopwords
from pymystem3 import Mystem
import string

#Lemmatizer
mystem = Mystem()
russian_stopwords = stopwords.words("russian")

#Read and parse
def get_words():
    with open('./Bulgakov.txt', 'r') as text_file:
        contents = text_file.read()
        # print(contents)

    translator = str.maketrans('', '', string.punctuation)
    clean_text = contents.translate(translator)
    clean_text = clean_text.replace('\n', ' ')
    # print(clean_text)





    # #Get list of words
    # word_list = clean_text.split(" ")
    # print(word_list)

    # sorted(word_list, key=lambda i: alphabet.index(i))

get_words()



