#ROT cipher

word = input("Please enter a word or phrase: ")
key_value = int(input("Please enter a key value (1-26): "))

numbers_set = []
encoded_set = []

cipher = {
    "a" : 0, "b": 1, "c" : 2, "d": 3, "e" : 4,
    "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j": 9,
    "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14,
    "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19,
    "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25
    }

def ROT13(word):
    chars = list(word)  
    print(chars)

    for i in range(0, len(chars), 1):
        for key, value in cipher.items():
            if chars[i] == key:
                numbers_set.insert(i, value)
    print(numbers_set, "letters to numbers")

    converted_set = [((num + key_value) % 26) for num in numbers_set]
    print(converted_set, "rotated by 13")

    for key, value in cipher.items():
        for i in range(0, len(converted_set), 1):
            if converted_set[i] == value:
                encoded_set.insert(i, key)
    print(encoded_set, "encoded set")

    encoded = ""
    encoded = encoded.join(encoded_set)
    print(f'The encoded message is: {encoded}')


ROT13(word)

