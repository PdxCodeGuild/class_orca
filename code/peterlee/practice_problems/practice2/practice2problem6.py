def count_letter(letter, word):
    return word.count(letter)

def main():
    input_word = input('Enter a word or string of letters: ')
    input_letter = input('Enter the letter you want to count in the word/string: ')
    print(count_letter(input_letter, input_word))

main()