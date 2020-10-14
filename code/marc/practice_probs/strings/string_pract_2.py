#String practice #2

# Write a function that takes a string, and returns a list of strings, each missing a different character.

# missing_char('kitten') → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

def missing_char(word):
    letters = list(word)
    print(letters)
    missing_letter = []
   
    
    letters.remove(1)
    print(letters)
        # new_word = "".join(new_letters)
        # missing_letter.append(new_word)
        
    return missing_letter

print(missing_char("kitten"))

