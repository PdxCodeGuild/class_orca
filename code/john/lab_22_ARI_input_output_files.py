##############################################################################
# John Fial, PDX Code Guild, 2020-2021 
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab22-ari.md
##############################################################################

# FILENAMES:
# testbook.txt
# carroll_alices_adventures_in_wonderland.txt
# jung_~1920_collected_papers_on_analytical_psychology.txt

import math # necessary for the math.ceil function to round up

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st/2nd Grade'},
     3: {'ages':   '7-9', 'grade_level':    '3rd Grade'},
     4: {'ages':   '9-10', 'grade_level':    '4th Grade'},
     5: {'ages':  '10-11', 'grade_level':    '5th Grade'},
     6: {'ages': '11-12', 'grade_level':    '6th Grade'},
     7: {'ages': '12-13', 'grade_level':    '7th Grade'},
     8: {'ages': '13-14', 'grade_level':    '8th Grade'},
     9: {'ages': '14-15', 'grade_level':    '9th Grade'},
    10: {'ages': '15-16', 'grade_level':    '10th Grade'},
    11: {'ages': '16-17', 'grade_level':   '11th Grade'},
    12: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-24', 'grade_level':      'College Student'},
    15: {'ages': '24+', 'grade_level':      'Professor'},
}

# This line makes it slightly simpler to change the filename
file_to_open = 'carroll_alices_adventures_in_wonderland.txt'

# Open file as UTF-9 and save it as a string 'book'
with open(file_to_open, 'r', encoding='utf-8') as f:
    book = f.read()
    # print(open(file_to_open, 'r')) # If you want to verify the encoding type

# Count the number of characters... 
characters = len(book)

# Count the number of words...split at space
words = book.count(' ')

# Count the number of sentences...split at periods
sentences = book.count('.')

# TEST ARI VALUES:
# characters = 1000.0
# words = 216.0
# sentences = 22.0

# This is the predefined ARI formula, see https://en.wikipedia.org/wiki/Automated_readability_index
ari_raw = ( 4.71 * ( characters/words ) + 0.5 * ( words / sentences ) - 21.43 )

# Round ari_raw up or leave at 14 if above 14
if ari_raw > 15:
    ari_rounded = 15
    impressive = 'Wow! That\'s an impressively high score! '
else:
    ari_rounded = math.ceil(ari_raw)
    impressive = ''

# Extract the scale data from the original dictionary
scale_data = ari_scale[ari_rounded]

ages = scale_data['ages']
grade_level = scale_data['grade_level']

# FINAL PRINT RESULT
print(f'''The raw ARI score for file:{file_to_open} is {ari_raw}, so its ARI value is {ari_rounded}. {impressive}\nThis value corresponds to a \"{grade_level}\" level of difficulty, suitable for the average person {ages} years old.''')








##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab22-ari.md
##############################################################################

# Lab 22: Compute Automated Readability Index

# Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

# ARI Formula

# The score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

# Scores correspond to the following ages and grad levels:

#     Score  Ages     Grade Level
#      1       5-6    Kindergarten
#      2       6-7    First Grade
#      3       7-8    Second Grade
#      4       8-9    Third Grade
#      5      9-10    Fourth Grade
#      6     10-11    Fifth Grade
#      7     11-12    Sixth Grade
#      8     12-13    Seventh Grade
#      9     13-14    Eighth Grade
#     10     14-15    Ninth Grade
#     11     15-16    Tenth Grade
#     12     16-17    Eleventh grade
#     13     17-18    Twelfth grade
#     14     18-22    College

# Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

# The output should look something like the following:

# --------------------------------------------------------

# The ARI for gettysburg-address.txt is 12
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.

# --------------------------------------------------------
