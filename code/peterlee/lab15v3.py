num = int(input('enter a number from 0-999: '))

#separates the digits to ensure we can convert them all into roman numerals
hundreds_digit = num//100
tens_digit = (num%100)//10
ones_digit = num%10



#creates lists for each digit for proper conversion
hundreds_list = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

tens_list = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']

ones_list = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

#prints appropriate conversion
if hundreds_digit == 0 and tens_digit == 0:
    print(ones_list[ones_digit])
elif hundreds_digit == 0 and tens_digit > 0 and ones_digit == 0:
    print(tens_list[tens_digit])
elif hundreds_digit > 0 and tens_digit == 0 and ones_digit == 0:
    print(hundreds_list[hundreds_digit])
elif hundreds_digit == 0 and tens_digit > 0 and ones_digit > 0:
    print(f'{tens_list[tens_digit]}{ones_list[ones_digit]}')
elif hundreds_digit > 0 and tens_digit == 0 and ones_digit > 0:
    print(f'{hundreds_list[hundreds_digit]}{ones_list[ones_digit]}')
elif hundreds_digit > 0 and tens_digit > 0 and ones_digit ==0:
    print(f'{hundreds_list[hundreds_digit]}{tens_list[tens_digit]}')
else:
    print(f'{hundreds_list[hundreds_digit]}{tens_list[tens_digit]}{ones_list[ones_digit]}')