# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('catdogcatdog') → True

def cat_dog(word):
    how_many_cat = 0
    how_many_dog = 0
    letters = list(word)
    # print(letters)
    for i in range(0, len(letters)-2):
        if letters[i] + letters[i + 1] + letters[i + 2] == "cat":
            how_many_cat += 1
    for i in range(0, len(letters)-2):
        if letters[i] + letters[i + 1] + letters[i + 2] == "dog":
            how_many_dog += 1
    if how_many_cat == how_many_dog:
        return True
    else:
        return False
print(cat_dog("catcatcatdogdogdog"))
            
    
  