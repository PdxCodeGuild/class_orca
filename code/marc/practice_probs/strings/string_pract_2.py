#String practice #2

# Write a function that takes a string, and returns a list of strings, each missing a different character.

# missing_char('kitten') → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

def missing_char(word):
    # print(letters)
    missing_letter = []
    
    for i in range (0, len(word)):
        man_letters = list(word)
        man_letters.pop(i)
        new_word = "".join(man_letters)
        missing_letter.append(new_word)
        
        
    return missing_letter

print(missing_char("kitten"))

