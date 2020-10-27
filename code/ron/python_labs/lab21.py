
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab21
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-13-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 21: Count Words

'''
#----Modules------------------------------------------------

import math
import string
import io

#----Global variables, lists, dictionaries------------------

words_dict = {}

text_f = "proposal.txt"

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 
'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 
'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 
'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 
'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 
'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 
'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 
'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 
'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 
'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 
'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 
'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 
'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 
'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 
"didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', 
"haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', 
"needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', 
"weren't", 'won', "won't", 'wouldn', "wouldn't"]

#----Functions----------------------------------------------

def strip(contents):
    '''Strip punctuation from raw contents '''
    translator = str.maketrans('', '', string.punctuation)
    new_chars = contents.translate(translator)
    return new_chars

def del_function(str_input):
    '''Delete any spaces or sentance breaks in text '''
    for x in range(len(str_input)):
        for i in str_input:
            if i in (" ", "\n"):
                str_input.remove(i)
    return str_input

def del_stopwords(new_contents):
    for i in range(len(new_contents)):
        for x in new_contents:
            if x in stopwords:
                new_contents.remove(x)
    return new_contents

#--------Main Code---------------------------------------------

def main(): 

    # Open file for reading
    with open(text_f) as f:
        contents = f.read()

    # Split text into list of words and do commented stuff: ---
    new_contents = contents.lower()              ## Lower case
    sentance_count = contents.count('.')         ## Sentance count
    new_contents = strip(new_contents)           ## Remove punctuation
    new_contents = new_contents.split()          ## Split into words
    new_contents = del_function(new_contents)    ## Remove spaces and line breaks
    word_count = len(new_contents)               ## Count words
    new_contents = del_stopwords(new_contents)   ## Rebuild list minus stopwords
    #-----------------------------------------------------------

    # Build word dictionary
    for x in range(len(new_contents)):
        if new_contents[x] not in words_dict.keys():
            words_dict[new_contents[x]] = 1
        elif new_contents[x] in words_dict.keys():
            words_dict[new_contents[x]] += 1

    # Print top 10 most mentioned words
    print(f'\n**** The top words mentioned in {text_f} ****\n')
    words = list(words_dict.items())                    # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)    # sort largest to smallest, based on count
    for i in range(min(10, len(words))):                # print the top 10 words, or all of them, whichever is smaller
        print(f'\t{words[i]}')

    # Misc. extra output
    print(f'\n\t No. of sentances: {sentance_count}')
    print(f'\t No. of words: {word_count} \n')


main()