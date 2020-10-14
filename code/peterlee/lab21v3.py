import string

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

    #removes non-alphabetic characters in list
    contents_list = [x for x in contents_list if str.isalpha(x)]

    #pairs words in contents_list in a tuple in a new list
    contents_list_paired_one = []
    for i in range (1, len(contents_list)):
        if i%2 == 1:
            b = (contents_list[i-1], contents_list[i])
            contents_list_paired_one.append(b) 
    
    contents_list_paired_two = []
    for i in range (2, len(contents_list)):
        if i%2 == 0:
            c = (contents_list[i-1], contents_list[i])
            contents_list_paired_two.append(c) 
 
    #adds word pairing:count from the list into a dictionary
    words_dict_one = {}
    for x in contents_list_paired_one:
        if x not in words_dict_one:
            words_dict_one[x] = 0
        words_dict_one[x] += 1

    words_dict_two = {}
    for x in contents_list_paired_two:
        if x not in words_dict_two:
            words_dict_two[x] = 0
        words_dict_two[x] += 1

    input_word = input('Enter a word: ')

    #prints the top 10 word pairs as shown in the lab instructions
    words_one = list(words_dict_one.items())

    words_two = list(words_dict_two.items())

    words = zip(words_one, words_two)

    updated_words = [x for x in words if x[0][0] == input_word]
    # updated_words.sort(key=lambda tup: tup[1], reverse=True)

    print(updated_words)
#     for i in range(min(10, len(words))):
#         print(words[i])

main()