# dictionary of single numbers plus teens
single = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen'
}
# dictionary of multiples of ten
tens = {
    0: 'zero', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
    6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
}

hundreds = {
    1: 'one hundred', 2: 'two hundred', 3: 'three hundred',
    4: 'four hundred', 5: 'five hundred', 6: 'six hundred',
    7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'
}

# getting input from user, module the number to get the 'ones' digit and 'tens' digit
x = int(input('enter number between 0-999\n>'))
ones_digit = x % 10
if x < 99:
    tens_digit = x // 10
else:
    tens_digit = int((x/10) % 10)
hundreds_digit = x // 100

# converting and returning the singles digit as a string
def convert_single(blah):
    for key in single:
        if blah == key:
            return single[key]

# converting and returning the tens digit as a string
def convert_ten(blah):
    for key in tens:
        if blah == key:
            return tens[key]

# converting and returning the hundreds digit as a string
def convert_hundred(blah):
    for key in hundreds:
        if blah == key:
            return hundreds[key]

# if x is already in the single dictionary, it will just print
for i in single:
    if x == i:
        print(single[i])

# checking all numbers over 19 and converting to strings using above functions
if x > 19:
    if convert_hundred(hundreds_digit):
        if convert_ten(tens_digit) == 'zero' and convert_single(ones_digit) == 'zero':
            print(convert_hundred(hundreds_digit))
        elif convert_ten(tens_digit) and convert_single(ones_digit) == 'zero':
            print(f'{convert_hundred(hundreds_digit)}-{convert_ten(tens_digit)}')
        elif convert_ten(tens_digit) == 'zero' and convert_single(ones_digit):
            print(f'{convert_hundred(hundreds_digit)}-{convert_single(ones_digit)}')
    else:
        if convert_ten(tens_digit) and convert_single(ones_digit) == 'zero':
            print(f'{convert_ten(tens_digit)}')
        else:
            print(f'{convert_ten(tens_digit)}-{convert_single(ones_digit)}')