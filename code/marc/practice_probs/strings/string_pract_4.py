# Write a function that returns the number of occurances of 'hi' in a given string.

# count_hi('hihi') → 2

def how_many_hi(word):
    how_many = 0
    letters = list(word)
    # print(letters)
    for i in range(0, len(letters)-1):
        if letters[i]+ letters[i + 1] == "hi":
            how_many += 1
            # print (how_many)
    return how_many
print(how_many_hi("hilohisenthi"))