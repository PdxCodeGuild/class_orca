ones = {
    0: '',
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    9: 'IX'
}
tens = {
    0: '',
    1: 'X',
    2: 'XX',
    3: 'XXX',
    4: 'XL',
    5: 'L',
    6: 'LX',
    7: 'LXX',
    8: 'XXC',
    9: 'XC',
}
hundreds = {
    0: '',
    1: 'C',
    2: 'CC',
    3: 'CCC',
    4: 'CD',
    5: 'D',
    6: 'DC',
    7: 'DCC',
    8: 'CCM',
    9: 'CM',
}

def one_thru_nine(user_input):
    user_ones = user_input % 10
    ones_conv = ones[user_ones]
    return ones_conv


def above20(user_input):
    user_tens = user_input // 10
    user_ones = user_input % 10
    tens_conv = tens[user_tens]
    ones_conv = ones[user_ones]
    return tens_conv

def hundreds_conv(user_input):
    user_hundreds = user_input // 100
    hundreds_conv = hundreds[user_hundreds]
    return hundreds_conv

    

# asking for a number
user_input = int(input('Please enter a numerical number between 1-999 to have it converted to Roamn numerals: '))
if user_input in range(1,10):
    ones_conv = one_thru_nine(user_input)
    print(f'Your number phrase is {ones_conv}!')

# converting for teens numbers


elif user_input in range(20,100):
    tens_conv = above20(user_input)
    ones_conv = one_thru_nine(user_input)
    print(f'Your number phrase is {tens_conv}{ones_conv}')
    
else:
    tens_digit = tens[user_input//10%10]
    ones_digit = ones[user_input%10]
    hundreds_digit = hundreds[user_input //100]
    print(f'Your number phrase is {hundreds_digit}{tens_digit}{ones_digit}!')