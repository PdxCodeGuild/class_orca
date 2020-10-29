# Welcome to lab21 by Quinton Baseman

import string
# creating a variable with a txt file as the value
with open('scratch.txt') as f:
    contents = f.read()

# removing all punctuation/uppercases and turning all words into a list
translator = str.maketrans('', '', string.punctuation)
string_without_punct = contents.translate(translator)
string_without_punct = string_without_punct.lower()

words = string_without_punct.split()

# excluding all of these words 
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
"you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 
'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 
'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 
'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 
'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 
'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 
'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 
'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 
'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 
'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 
'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 
've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 
'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 
'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 
'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'mr']

# creating an empty dictionary to add key(words) value(occurences) pairs
word_count = {}

# sorting through the list of words. if the word is not in the dictionary AND not in stop words,
# it gets added as a key, plus counts up the value
for i in words:
    if i not in stop_words:
        if i in word_count.keys():
            word_count[i] += 1
        else:
            word_count[i] = 1

# sorting all of the words, getting the top ten words
sorted_words = sorted(word_count.items(), key=lambda kv: kv[1])
top_words = sorted_words[::-1]
top_ten = top_words[0:10]

first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth = top_ten[0][0], top_ten[1][0], \
    top_ten[2][0], top_ten[3][0], top_ten[4][0], top_ten[5][0], top_ten[6][0], top_ten[7][0], top_ten[8][0], top_ten[9][0]
num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = top_ten[0][1], top_ten[1][1], top_ten[2][1], \
    top_ten[3][1], top_ten[4][1], top_ten[5][1], top_ten[6][1], top_ten[7][1], top_ten[8][1], top_ten[9][1]

print(f'''

Top ten most common words
-------------------------
1st: {first} - {num1} times
2nd: {second} - {num2} times
3rd: {third} - {num3} times
4th: {fourth} - {num4} times
5th: {fifth} - {num5} times
6th: {sixth} - {num6} times
7th: {seventh} - {num7} times
8th: {eighth} - {num8} times
9th: {ninth} - {num9} times
10th: {tenth} - {num10} times


''')

f.close()