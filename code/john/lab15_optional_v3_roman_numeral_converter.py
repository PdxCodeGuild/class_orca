##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab15-number_to_phrase.md
##############################################################################

# Welcome
print('Welcome to number to roman numerals converter v1!')

numerical_phrases = {
    0: '0',    1: 'I',    2: 'II',    3: 'III',    4: 'IV',    
    5: 'V',    6: 'VI',    7: 'VII',    8: 'VIII',    9: 'IX',
    10: 'X',    11: 'XI',    12: 'XII',    13: 'XIII',    14: 'XIV',
    15: 'XV',    16: 'XVI',    17: 'XVII',    18: 'XVIII',    19: 'XIX',
    20: 'XX',    30: 'XXX',    40: 'XL',        
    50: 'L',    60: 'LX',    70: 'LXX',    80: 'LXXX',    90: 'XC',    
    100: 'C',    200: 'CC',    300: 'CCC',    400: 'CD',
    500: 'D',    600: 'DC',    700: 'DCC',    800: 'DCCC',    900: 'CM',
    1000: 'M',    2000: 'MM',    3000: 'MMM',
}


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
        hundreds_phrase = numerical_phrases.get(hundreds_digit*100) + ' '

    final_two_digits = (input_number - ( hundreds_digit * 100 ))

    #Adjust if final digits ends in 00:
    if final_two_digits == 00:
        hundreds_phrase = numerical_phrases.get(hundreds_digit)
        final_numerical_phrase = f'{hundreds_phrase} {tens_phrase}'
        print(f'The number {input_number} is written as "{final_numerical_phrase}."')
        
    # If it's something-hundred and an exact dictionary number, simply concatenate those two...
    elif final_two_digits in numerical_phrases:

        tens_phrase = numerical_phrases.get(final_two_digits) # kind of cheating with this variable name...
        final_numerical_phrase = f'{hundreds_phrase}{tens_phrase}'
        print(f'The number {input_number} is written as "{final_numerical_phrase}."')

    # Otherwise concatenate all three phrases
    else:
        # Add the dash - for the tens phrase of non-dictionary items
        tens_phrase = numerical_phrases.get(tens_digit*10)             
        ones_phrase = numerical_phrases.get(ones_digit)
        final_numerical_phrase = f'{hundreds_phrase}{tens_phrase} {ones_phrase}'
        print(f'The number {input_number} is written as "{final_numerical_phrase}."')
