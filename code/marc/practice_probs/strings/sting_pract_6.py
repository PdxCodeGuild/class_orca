# Return the number of letter occurances in a string.

# def count_letter(letter, word):
#     ...
# count_letter('i', 'antidisestablishmentterianism') → 5
# count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') → 2

def letter_counter(letter, word):
    number_of_letter = 0
    for i in range(len(word)):
        if word[i] == letter:
            number_of_letter += 1
    return number_of_letter
print(letter_counter("d", "dodge"))