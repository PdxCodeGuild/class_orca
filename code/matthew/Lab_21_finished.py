"""
lab 21
Matthew Chimenti
"""


dic_words = {

}


with open('dracula.txt', 'r') as get_file:
    contents = get_file.read()

import string
s = contents
translator = str.maketrans('', '', string.punctuation)
string_without_punct = s.translate(translator) # I am a string with punctuation
# print(string_without_punct)

# lowercase all the letters
lower_str = string_without_punct.lower()
# print(lower_str)

# Make the words into a list
words = lower_str.split()
# print(words)

# put list into dict. If in list +1
for word in words:
    if word not in dic_words:
        # print(word)
        dic_words[word] = 1
    elif word in dic_words:
        dic_words[word] += 1
# print(dic_words)

#make the dictionary a view object containing key value pairs
word_count = list(dic_words.items())


word_count.sort(key=lambda tup: tup[1], reverse=True)

# print the 10 words
for i in range(min(10, len(word_count))):
    print(word_count[i])