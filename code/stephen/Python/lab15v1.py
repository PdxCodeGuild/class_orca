# LAB 15 - Number to Phrase v1

# creating libraries for tens, teens and hundreds
hundreds = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

tens = {
    1: '',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

outliers = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}



def one_thru_nine(user_input):
    user_hundreds = user_input % 10
    hundreds_conv = hundreds[user_hundreds]
    return hundreds_conv

def ten_thru_20(user_input):
    converted = outliers[user_input]
    print(f'Your number phrase is {converted}!')

def above20(user_input):
    user_tens = user_input // 10
    user_hundreds = user_input % 10
    tens_conv = tens[user_tens]
    hundreds_conv = hundreds[user_hundreds]
    return tens_conv



    

# asking for a number
user_input = int(input('Please enter a numerical number between 1-99 to have it converted to a phrase: '))

if user_input in range(1,10):
    hundreds_conv = one_thru_nine(user_input)
    print(f'Your number phrase is {hundreds_conv}!')

# converting for teens numbers

if user_input in range(10,20):
    ten_thru_20(user_input)

if user_input in range(20,100):
    tens_conv = above20(user_input)
    hundreds_conv = one_thru_nine(user_input)
    print(f'Your number phrase is {tens_conv}-{hundreds_conv}')
    
