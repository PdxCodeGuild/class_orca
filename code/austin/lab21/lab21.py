#Lab 21: Count Words

import string

def top_10():
    with open('./pygmalion.txt', 'r') as text_file:
        contents = text_file.read()
        # print(contents)

    translator = str.maketrans('', '', string.punctuation)
    clean_text = contents.translate(translator)
    clean_text = clean_text.replace('\n', ' ')
    clean_text = clean_text.lower()
    # print(clean_text)

    word_list = clean_text.split(" ")
    # print(word_list)

    #Exclude common words

    stop_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "the", "and", " ", ""]

    word_list = [x for x in word_list if x not in stop_list]

    #Get top 10 words in book

    word_counts = {}

    for word in word_list:
        if word not in word_counts:
            word_counts[word] = 1
        else: 
            word_counts[word] += 1
    
    words = list(word_counts.items())

    words.sort(key=lambda tup:tup[1], reverse=True)

    top_ten = []
    for i in range(10):
        top_ten.append(words[i])

    top_ten = dict(top_ten)

    print("The top ten words in Pygmalion are: ")
    for key, value in top_ten.items():
        print(key, ':', ' ', value)

top_10()