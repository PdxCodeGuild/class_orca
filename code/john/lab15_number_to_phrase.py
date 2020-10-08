##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab15-number_to_phrase.md
##############################################################################

# Welcome
print('Welcome!')

numerical_phrases = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred', #it's not "one-hundred" because the function will fill in the number-hundred
}

    # Once working, TEMP COMMENT OUT that input, and set the user number to your own value for now
    # input_number = input('Please enter a single number from 0-999, without decimals or fractions: ')
    # print(input_number)

input_number = 167 ######################### test number

#  Check if that user's exact value is in the dictionary, if so, simply print out the exact phrase
if input_number in numerical_phrases:
    # print('   DICTIONARY LOOKUP found it! what an unusual number!') # REMOVE
    final_numerical_phrase = ''
    final_numerical_phrase += numerical_phrases.get(input_number)
    print(f'The number {input_number} is written as "{final_numerical_phrase}."')
else:
    # print('     elsed')

    # Here we have to break the number up into its individual components
    # FIX in future, because going through character by character might be better
    hundreds_digit = input_number // 100
    tens_digit = (input_number - ( hundreds_digit * 100 )) // 10 # Here we have to subtract all the hundreds place out, then take the floor dividend...
    ones_digit = input_number % 10

    if hundreds_digit == 0:
        hundreds_phrase = ''
    else:
        hundreds_phrase = numerical_phrases.get(hundreds_digit) + '-hundred and '

    if tens_digit == 0:
        tens_phrase = ''
    else:
        tens_phrase = numerical_phrases.get(tens_digit*10) + '-'

    ones_phrase = numerical_phrases.get(ones_digit)

    final_numerical_phrase = f'{hundreds_phrase}{tens_phrase}{ones_phrase}'
    
    print(f'The number {input_number} is written as "{final_numerical_phrase}."')












# print('     end')
# END


##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab15-number_to_phrase.md
##############################################################################
# Lab 15: Number to Phrase

# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.

# x = 67
# tens_digit = x//10
# ones_digit = x%10

# Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.
# Version 2

# Handle numbers from 100-999.
# Version 3 (optional)

# Convert a number to roman numerals.
# Version 4 (optional)

# Convert a time given in hours and minutes to a phrase.