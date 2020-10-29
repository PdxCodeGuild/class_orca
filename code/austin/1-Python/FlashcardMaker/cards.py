#Anki Automated Flashcard Maker

import nltk
# nltk.download("stopwords")
import json
from nltk.corpus import stopwords
from pymystem3 import Mystem
import string
from string import punctuation


#Russian punctuation
russian_punc = "!;№-«»–…"

#Read and parse
def get_words():
    with open('./sobache-serdce.txt', 'r') as text_file:
        contents = text_file.read()
        contents = contents.lower()

        for punc in contents:
            if punc in russian_punc:
                contents = contents.replace(punc, "")
        # print(contents)
    
    #Lemmatizer
    mystem = Mystem()
    lemmas = mystem.lemmatize(contents)
    clean_text = ''.join(lemmas)
    # print(clean_text)

    #Get rid of all spaces and punctuation
    translator = str.maketrans('', '', string.punctuation)
    clean_text = contents.translate(translator)
    clean_text = clean_text.replace('\n', '')
    # print(clean_text)

    # #Get list of words
    word_list = clean_text.split(" ")
    word_list = [word for word in word_list if word != " " or word != ""]
    # print(word_list)

    #Get rid of stop words
    russian_stopwords = stopwords.words("russian")
    word_list = [x for x in word_list if x not in russian_stopwords]
    # print(word_list)

    #Get rid of duplicates
    no_dupes = []
    [no_dupes.append(x) for x in word_list if x not in no_dupes]
    # print(no_dupes)

    #Get info
    word_info = json.dumps(mystem.analyze(clean_text), ensure_ascii=False)
    print(word_info)

    # #Get word stems
    # stems = []
    # stemmer = SnowballStemmer("russian")
    # for token in no_dupes:
    #     token = stemmer.stem(token)
    #     if token != "":
    #         stems.append(token)
    # print(stems)

    # clean_text = mystem.lemmatize(contents.lower())
    # tokens = [token for token in tokens if token not in russian_stopwords\
    #             and token != " " \
    #             and token.strip not in punctuation]
    
    # sorted(word_list, key=lambda i: alphabet.index(i))



get_words()



