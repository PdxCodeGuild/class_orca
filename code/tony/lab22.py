import string
reader = 'gettysburg.txt'
text = open(file=reader).read()

def punc_stripper(to_strip):
    punct_stripper = to_strip.translate(str.maketrans('','',string.punctuation))
    return punct_stripper
score = 0
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# ---------- sentences
# sentences split by space after new lines
sentences = text.split('.')

# remove space
while '' in sentences:
    sentences.remove('')

# remove newlines
for i,x in enumerate(sentences):
    sentences[i] = x.strip('\n')

# ------ number of sentences ------
nu_sentences = len(sentences)


# ----------- words
# strip text of punctuation
stripped = punc_stripper(text)

# split into words
words = stripped.split()

# ----- number of words -----
nu_words = len(words)


# ---------- characters
chars = 0
# ---- number of characters in words
for x in words:
    chars += len(x)

print(f'{nu_sentences} sentences, {nu_words} words, {chars} characters.')

score = round(4.71*(chars/nu_words) + 0.5*(nu_words/nu_sentences) - 21.43)
if score > 14:
    score = 14

print(f'ARI for {reader} is {score}')
print(f"This is text is {ari_scale[score]['grade_level']} level, suitable for people {ari_scale[score]['ages']} years old.")