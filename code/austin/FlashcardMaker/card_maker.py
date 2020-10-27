import nltk
nltk.download("stopwords")
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import string
from string import punctuation

import stanza
stanza.download('ru') 
nlp = stanza.Pipeline(lang="ru", processors='tokenize, pos, lemma')

import csv
import requests
import json

russianStemmer=SnowballStemmer("russian", ignore_stopwords=True)
wordnet_lemmatizer = WordNetLemmatizer()

#Russian punctuation
russian_punc = "!;№-«»–…?.""''%^'-$*"

#Read and parse
def get_words():
    with open('./test_file.txt', 'r') as text_file:
        contents = text_file.read()
        contents = contents.lower()

    for punc in contents:
            if punc in russian_punc:
                contents = contents.replace(punc, "")
        # print(contents)
    
    #Get rid of all spaces and punctuation
    translator = str.maketrans('', '', string.punctuation)
    clean_text = contents.translate(translator)
    clean_text = clean_text.replace('\n', '')
    # print(clean_text)

    doc = nlp(clean_text)

    # print(*[f'word: {word.text+" "} \tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')

    #Get list of lemmas
    word_list = [word.lemma for sent in doc.sentences for word in sent.words]
    # print(word_list)

    #Get rid of stop words
    russian_stopwords = stopwords.words("russian")
    word_list = [x for x in word_list if x not in russian_stopwords]
    # print(word_list)

    #Get rid of duplicates
    no_dupes = []
    [no_dupes.append([x]) for x in word_list if x not in no_dupes]
    # print(no_dupes)

    #Get definitions, call to Yandex dictionary API

    def_responses = list()

    for word in no_dupes:
        response = requests.get(f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20201026T201332Z.a4a55e75eb125931.8cc488a85be2c2c17bfd363de1858a3aaef55d62&lang=ru-en&text={word[0]}")
        data = json.loads(response.text)
        # print(data)
        if data['def'] != []:
            def_responses.append(data)

        # print(response.status_code)
        # print(response.json())
    
    # print(def_responses)

    # This is the def
    defs = []
    for i in range(len(def_responses)):
        defs.append(def_responses[i]['def'][0]['tr'][0]['text'])
    print(defs)

    # zipped = list(zip(no_dupes, defs))
    # print(zipped)

    #Write to csv file
    fields = ['Word']
    with open('vocab_file.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(no_dupes)

get_words()

