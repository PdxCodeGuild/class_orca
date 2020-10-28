##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab15-number_to_phrase.md
##############################################################################

# Welcome
print('Welcome to number to phrase converter v1!')

numerical_phrases = {
    0: 'zero',    1: 'one',    2: 'two',    3: 'three',    4: 'four',    
    5: 'five',    6: 'six',    7: 'seven',    8: 'eight',    9: 'nine',
    10: 'ten',    11: 'eleven',    12: 'twelve',    13: 'thirteen',    14: 'fourteen',
    15: 'fifteen',    16: 'sixteen',    17: 'seventeen',    18: 'eighteen',    19: 'nineteen',
    20: 'twenty',    30: 'thirty',    40: 'fourty',        
    50: 'fifty',    60: 'sixty',    70: 'seventy',    
    80: 'eighty',    90: 'ninety',    100: 'one-hundred',
}

# ask user for their number
input_number = input('Please enter a single number from 0-999, without decimals or fractions: ')
#convert to a string
input_number = int(input_number)

final_numerical_phrase = ''

# MAIN CODE HERE
#  Check if that user's exact value is in the dictionary...
if input_number in numerical_phrases:
    final_numerical_phrase += numerical_phrases.get(input_number)
    print(f'The number {input_number} is written as "{final_numerical_phrase}."')
else:
    # ... if not, we have to break the number up into its individual components
    hundreds_digit = input_number // 100
    tens_digit = (input_number - ( hundreds_digit * 100 )) // 10 # Here we have to subtract all the hundreds place out, then take the floor dividend...
    ones_digit = input_number % 10

    hundreds_phrase = ''
    tens_phrase = ''
    ones_phrase = ''
    
    # Get the hundreds phrase
    if hundreds_digit == 0:
        pass 
    else:
        hundreds_phrase = numerical_phrases.get(hundreds_digit) + '-hundred and '

    final_two_digits = (input_number - ( hundreds_digit * 100 ))

# **************************************** WORKING FROM HERE *******************************
    #Adjust if final digits ends in 00:
    if final_two_digits == 00:
        hundreds_phrase = numerical_phrases.get(hundreds_digit) + '-hundred' # OVERWRITE the previous hundreds_phrase with the word " and ", because now we don't want it!
        final_numerical_phrase = f'{hundreds_phrase}{tens_phrase}'
        print(f'The number {input_number} is written as "{final_numerical_phrase}."')
    
    # If it's something-hundred and an exact dictionary number, simply concatenate those two...
    elif final_two_digits in numerical_phrases:
        tens_phrase = numerical_phrases.get(final_two_digits) # kind of cheating with this variable name...
        final_numerical_phrase = f'{hundreds_phrase}{tens_phrase}'
        print(f'The number {input_number} is written as "{final_numerical_phrase}."')

    # Otherwise concatenate all three phrases
    else:
        # Add the dash - for the tens phrase of non-dictionary items
        tens_phrase = numerical_phrases.get(tens_digit*10) + '-'               
        ones_phrase = numerical_phrases.get(ones_digit)

        final_numerical_phrase = f'{hundreds_phrase}{tens_phrase}{ones_phrase}'
        print(f'The number {input_number} is written as "{final_numerical_phrase}."')


# ****************************************  TO HERE ****************************************

