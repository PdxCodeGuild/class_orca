# imports
import string

STOPWORDS = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 
    'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 
    'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 
    'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 
    'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 
    'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 
    'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 
    'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 
    'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 
    'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
    'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 
    'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', 
    "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 
    'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 
    'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 
    'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 
    'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
]

def active_file(file):
    '''Call .txt file for manipulation'''
    with open(file, 'r') as f:
        contents = f.read()
        return contents

def text_scrub(contents):
    '''Convert text to all lower case, strip puncuation, 
    and split into a list of words.'''
    new_contents = contents.lower()
    newer_contents = str.maketrans('', '', string.punctuation + "’—“”")
    newest_content = new_contents.translate(newer_contents)
    newest_content = newest_content.split()
    # for item in newest_content:
    #     if item in STOPWORDS:
    #         newest_content.remove(item)
    # return newest_content 
    new_list = []
    for item in newest_content:
        if item not in STOPWORDS:
            new_list.append(item)
    return new_list

def dictionary(content):
    '''Quantifies each occurance of a word in a string of text and populates 
    a dictionary with the word as a key and the number as the value'''
    dictionary = {}
    for item in content:
        if item not in dictionary:
            dictionary[item] = 1
        if item in dictionary:
            dictionary[item] += 1
    return dictionary 

def count_words(populated_dict):
    '''Organizes a list of keywords and their occurances(values) into a list of the top 10 occurances'''
    words = list(populated_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    top_words = []
    for i in range(min(10, len(words))):
        top_words.append(words[i])
    return top_words

def main():
    contents = active_file('count_of_monte_cristo.txt')
    stripped_text = text_scrub(contents)
    populated_dict = dictionary(stripped_text)
    word_count = count_words(populated_dict)
    print(word_count)

main()