import string

digits_list = list(string.digits)

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
'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', 
"weren't", 'won', "won't", 'wouldn', "wouldn't"]

def main():
    with open('63444-0.txt', 'r', encoding='utf-8') as f:
        contents = f.read()

    #makes the text lowercase
    contents_lowercase = contents.lower()

    #strips punctuation from the text as shown in the lab instructions
    punctuation_stripper = str.maketrans('', '', string.punctuation)
    contents_strippedof_punctuation = contents_lowercase.translate(punctuation_stripper)

    #turns the text into a list of words
    contents_list = contents_strippedof_punctuation.split()

    #removes STOPWORDS from the list
    contents_list = [x for x in contents_list if x not in STOPWORDS]

    #removes non-alphabetic characters in list
    contents_list = [x for x in contents_list if str.isalpha(x)]

    #adds word:count from the list into a dictionary
    words_dict = {}
    for x in contents_list:
        if x not in words_dict:
            words_dict[x] = 0
        words_dict[x] += 1

    #prints the top 10 words as shown in the lab instructions
    words = list(words_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)

    for i in range(min(10, len(words))):
        print(words[i])

main()