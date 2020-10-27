from string import ascii_lowercase
from string import punctuation

# asking for phrase
user_word = input('Enter a phrase to encrypt:\n>').lower()

# asking for amount to decipher
amount = int(input('Enter an amount you would like to cipher by:\n>'))

def rot13(user_word):
    
    # empty output string
    encrypt = ''

    # adding to empty string and applying rotation, keep spaces, numbers and punctuation
    for x in user_word:
        if x in ascii_lowercase:
            encrypt += ascii_lowercase[(ascii_lowercase.index(x) + (amount)) % 26]
        if x.isnumeric():
            encrypt += x
        if x in punctuation:
            encrypt += x
        if x == ' ': 
            encrypt += ' '
    


    print(f'Your encrypted phrase is: {encrypt}')

rot13(user_word)

