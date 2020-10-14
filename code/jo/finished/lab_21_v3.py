# imports string to pull punctuation later
import string

# opens the book from txt file, sets it to read, and encodes it then saves to a variable
with open('frankenstein.txt', 'r', encoding='utf8') as t:
    text = t.read()

    # words that will be removed to not be counted
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    
    # empty dict that will get populated with words from the text and how often they are used
    word_dict = {}

    # these lines make the text all lower case; removes punctuation, newlines, and spaces; and removes stopwords and empty elements
    lower_text = text.lower() 
    translator = str.maketrans('', '', string.punctuation)
    punct_text = lower_text.translate(translator)
    deline_text = punct_text.replace('\n', ' ')
    split_text = deline_text.split(' ')
    split_text = [word for word in split_text if word not in stopwords]
    split_text = [word for word in split_text if word != '']

    # gets a word to check for
    ask = input('Enter a word to find the words that follow it: ')

    # empty lists to add to
    double_list1 = []
    double_list2 = []

    # checks text for matches with the input word. appends one list with the word for each usage. 
    # gets the index of each usage and adds 1 to get the words that follow each usage. appends the other list with them
    for word in split_text:
        if word == ask:
            double_list1.append(word)
            double_list2 = [split_text[i+1] for i,word in enumerate(split_text) if word == ask]
    
    # compines both lists into a list of tuples
    tuple_list = list(zip(double_list1, double_list2))

    # compares each tuple to keys in the dictionary. if not in the dict, it adds it with a value of 1. otherwise, it adds 1 to value, representing times it was used
    for word in tuple_list:
        if word not in word_dict:
            word_dict[word] = 1
        elif word in word_dict:
            word_dict[word] += 1

    # prints out the 10 most often used combos
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    
