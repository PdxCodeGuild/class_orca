def double_letters(user_input):
    user_input = list(user_input)
    for x in user_input:
        user_input = x * 2
        user_input = str(user_input)
        
        print(user_input)

# user_input = input('Enter in a word to double it:\n')

# double_letters(user_input)


def missing_char(word):
    word = list(word)
    i = 0
    for i in range(len(word[i])):
        
        new_word = []
        new_word = word.pop([i])
        word = str(word)
        print(word)
        i += 1


    


word = input('Enter a word:')
missing_char(word)

   