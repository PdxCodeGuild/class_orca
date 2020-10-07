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
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
    6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
}

# getting input from user, module the number to get the 'ones' digit and 'tens' digit
x = int(input('enter number between 0-99\n>'))
ones_digit = x % 10
tens_digit = x // 10
hundreds_digit = x // 100

# converting and returning the singles digit as a string
def convert_single(blah):
    for key in single:
        if blah == key:
            return single[key]

# converting and returning the tens digit as a string
def convert_tens(blah):
    for key in tens:
        if blah == key:
            return tens[key]

# if x is already in the single dictionary, it will just print
for i in single:
    if x == i:
        print(single[i])
# checking all numbers over 19 and converting to strings using above functions
while x > 19:
    if convert_single(ones_digit) == 'zero' and convert_tens(tens_digit):
        print(convert_tens(tens_digit))
        break
    else:
        print(f'{convert_tens(tens_digit)}-{convert_single(ones_digit)}')
        break