import string

with open('63444-0.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

contents_lowercase = contents.lower()

punctuation_stripper = str.maketrans('', '', string.punctuation)
contents_strippedof_punctuation = contents_lowercase.translate(punctuation_stripper)

contents_list = contents_strippedof_punctuation.split()

word_dict = {x: contents_list.count(x) for x in contents_list}

print(word_dict)

