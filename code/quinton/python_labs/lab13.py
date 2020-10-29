# Welcome to lab13 by Quinton Baseman

# getting input from user
user = input('Please enter anything you want\n>')
blank_list = []
# english to ROT dictionary
english_rot = {
    'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
    'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y',
    'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e',
    's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
    'y': 'l', 'z': 'm',
    'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
    'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y',
    'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E',
    'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K',
    'Y': 'L', 'Z': 'M'
}

# converts each letter from the input the user gave to the ROT translation
def convert(blah):
    for key in english_rot:
        if key == blah:
            return english_rot[key]

# sorts through characters/spaces/numbers/punctuation
new_phrase = ''
for i in user:
    if i.isalpha():
        new_phrase += convert(i)
    elif i == ' ':
        new_phrase += ' '
    else:
        new_phrase += i
# prints out your translated string
print(new_phrase)