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

    #pairs staggered words in another list in a tuple in a new list to make sure all pairings are accounted for
    contents_list_paired_two = []
    for i in range (2, len(contents_list)):
        if i%2 == 0:
            c = (contents_list[i-1], contents_list[i])
            contents_list_paired_two.append(c) 
    contents_list_combined = contents_list_paired_one + contents_list_paired_two
 
    #adds word pairing:count from the list into a dictionary
    words_dict = {}
    for x in contents_list_combined:
        if x not in words_dict:
            words_dict[x] = 0
        words_dict[x] += 1


    input_word = input('Enter a word: ')

    words = list(words_dict.items())

    #creates a new list that only contains the input word followed by another word
    words_list = [x for x in words if x[0][0] == input_word]
    #prints the top 10 words pairing as shown in the lab instructions
    words_list.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words_list))):
        print(words_list[i])

main()  