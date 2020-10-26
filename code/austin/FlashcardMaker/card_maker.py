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

russianStemmer=SnowballStemmer("russian", ignore_stopwords=True)
wordnet_lemmatizer = WordNetLemmatizer()

#Russian punctuation
russian_punc = "!;№-«»–…?.""''%^'-$*"

#Read and parse
def get_words():
    with open('./sobache-serdce.txt', 'r') as text_file:
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
    [no_dupes.append(x) for x in word_list if x not in no_dupes]
    # print(no_dupes)

    for i in range(len(no_dupes)):
        row_data = no_dupes[i], '\n'

    #Write to csv file
    fields = ['Word', 'Definition']
    rows = [row_data]
    with open('vocab_file.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(rows)
get_words()

