import string


with open('dracula.txt') as book:
    dracula = book.read()



STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 
'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 
'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 
'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 
'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 
'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 
'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 
'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 
'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 
'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 
'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 
'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", '', 'said', 'could', 'us', 'would', 'may', 'shall']


# makes text lowercase
dracula = dracula.lower()

translator = str.maketrans('', '', string.punctuation)
no_punct = dracula.translate(translator)

# replacing new line with spaces, splitting into list at space
no_punct =  no_punct.replace('\n', ' ')
no_punct = no_punct.split(' ')

# list comprehension to compare new_list to stopwords, delete any matches
new_list = [x for x in no_punct if x not in STOPWORDS]

# using zip and line splicing to create a list of tuples with the word ahead of it
pairs = dict(zip(new_list, new_list[1:] + new_list[:1]))

# print(list_of_values)

# making empty dict to input each word at key and how many times the word occurs as value
# word_dict = {}

# # looping through tuples to add to dictionary 
# for value in pairs:
    
#     if value not in word_dict.keys():
#         word_dict[value] = 1
    
#     else:
#         word_dict[value] += 1

# # user_input = input('Enter a word:\n>')

# # if user_input in pairs(keys):
    


# words = list(word_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# # words = dict(words)
# # if user_input in words.keys():

# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])


# # take input
# # ensure input is in book
# # compile dict of pairs
# # iterate through and count the matches of values
# # sort them highest to lowest

# while user_input in word_dict[x]:

def count(pairs): 
      
    pairs_count = {} 
    for i in pairs: 
        pairs_count[i] = pairs_count.get(i, 0) +1
    print(pairs_count) 

count(pairs)