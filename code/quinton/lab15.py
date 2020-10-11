# Welcome to lab15 by Quinton Baseman

# getting the input from the user
x = int(input('Enter a number between 0-999\n>'))
# key value pairs for ones, tens, hundreds digit. plus extra dictionary for 10-19
ones = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
weirds = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
          16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
hundreds = {1: 'One Hundred', 2: 'Two Hundred', 3: 'Three Hundred', 4: 'Four Hundred', 5: 'Five Hundred',
            6: 'Six Hundred', 7: 'Seven Hundred', 8: 'Eight Hundred', 9: 'Nine Hundred'}
# manipulating digits to determine which dictionaries to use
ones_digit = x % 10
if x < 99:
    tens_digit = x // 10
else:
    tens_digit = int((x/10) % 10)
hundreds_digit = x // 100

# converting the one digit
def convert_one(blah):
    for key in ones:
        if blah == key:
            return ones[key]

# converting the ten digit
def convert_ten(blah):
    for key in tens:
        if blah == key:
            return tens[key]

# converting the hundred digit
def convert_hundred(blah):
    for key in hundreds:
        if blah == key:
            return hundreds[key]

# checking if the digit is in the weird dictionary
def weird_digit(blah):
    if blah > 99:
        if 10 <= blah % 100 <= 19:
            i = blah % 100
            return f'{hundreds[hundreds_digit]} {weirds[i]}'
        else:
            return False

# if number is in the weird dictionary, it will print
if 10 <= x <= 19:
    for key in weirds:
        if x == key:
            print(weirds[key])
# checking which dictionary combo is needed for the correct output
else:
    if not weird_digit(x):
        if convert_hundred(hundreds_digit):
            if convert_ten(tens_digit):
                if convert_one(ones_digit) != 'Zero':
                    print(hundreds[hundreds_digit], tens[tens_digit], ones[ones_digit])
                else:
                    print(hundreds[hundreds_digit], tens[tens_digit])
            else:
                if convert_one(ones_digit) != 'Zero':
                    print(hundreds[hundreds_digit], ones[ones_digit])
                else:
                    print(hundreds[hundreds_digit])
        else:
            if convert_ten(tens_digit):
                if convert_one(ones_digit) != 'Zero':
                    print(tens[tens_digit], ones[ones_digit])
                else:
                    print(tens[tens_digit])
            else:
                print(ones[ones_digit])
    else:
        print(weird_digit(x))