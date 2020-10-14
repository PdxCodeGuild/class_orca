#Return the letter that appears the latest in the english alphabet.

# >>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
# the latest letter is v.

def latest_letter(word):
    ordered_list = list(reversed(sorted(word)))
    last_letter = ordered_list[0]
    return last_letter


print(latest_letter("iusreguisbggurbgeubrgb"))
