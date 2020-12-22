'''
Lab 13
Matthew Chimenti
'''


english_rot = {
    'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
    'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y',
    'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e',
    's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
    'y': 'l', 'z': 'm',
}

output = []

user_input = list(input("Please enter a word "))

for letter in user_input:
    if letter in english_rot:
        output.append(english_rot[letter])

print(*output)

