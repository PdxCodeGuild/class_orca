# dictionaries for ones and tens units.
spell_tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fivety',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

spell_singles = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

# dictionary for the abnormally spelled teens
spell_teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteeyn',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

# ask for user input. input becomes number to spell
number = int(input('Please enter a number: '))

# if number is 10-19, prints from teen dictionary, if less than 9, prints from singles, 
# else it splits the number into ones and tens and combines and prints them
if 10 <= number <=19:
    teens = spell_teens[number]
    print(f"{number} is spelled {teens}")

elif number <= 9:
    singles = spell_singles[number]
    print(f"{number} is spelled {singles}")

elif 20 <= number <= 99:
    tens_digit = (number//10)
    ones_digit = (number%10)

    if 1 <= ones_digit <= 9:
        tens_digit = spell_tens[tens_digit]
        ones_digit = spell_singles[ones_digit]
        print(f"{number} is spelled {tens_digit}-{ones_digit}")
    else:
        tens_digit = spell_tens[tens_digit]
        print(f"{number} is spelled {tens_digit}")
   
else:
    tens_digit = spell_tens[number//10%10]
    ones_digit = spell_singles[number%10]
    hundreds_digit = spell_singles[number//100]
    print(f"{number} is spelled {hundreds_digit} hundred {tens_digit}-{ones_digit}")