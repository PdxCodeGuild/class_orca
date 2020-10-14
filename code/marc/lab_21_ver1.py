#This is Lab 21 word count
#1 Import a book in the form of a txt file from guttenberg
#2 Make everything lowercase, strip punctuation, split into a list of words.
#3 Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
#4 Print the most frequent top 10 out with their counts. You can do that with the code below.
#5 You'll find that the most common words aren't particularly interesting (lots of 'I's, 'the', 'and', 'he', 'she', and 'but's). To get more relevant words, remove stop words from your text.
def main():
    import string
    with open('Edible Toadstools and Mushrooms.txt', 'r') as mushroom_book:
        contents = mushroom_book.read()
    words = contents.strip().lower().translate(str.maketrans(' ', ' ', string.punctuation)).split()
    # print(words)
    STOPWORDS = ['the', 'is', 'its', 'a', 'this', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    
    # for word in words:
    #     if word in STOPWORDS:
    #         words.remove(word)
    words = [word for word in words if word not in STOPWORDS] #this worked better at sorting then the above code
    
    word_count = {}

    for word in words:
        if word not in word_count:
            word_count[word] = 1
        if word in word_count:
            word_count[word] += 1
    
    top_ten = list(word_count.items()) # .items() returns a list of tuples
    top_ten.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(top_ten))):  # print the top 10 words, or all of them, whichever is smaller
        print(top_ten[i])
       
    # print(word_count)

main()