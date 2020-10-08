num = int(input('enter a number from 0-999: '))

#separates the digits to ensure we can convert them into words
hundreds_digit = num//100
tens_digit = (num%100)//10
ones_digit = num%10



#creates lists of prefixes, suffixes, and standalone words that we can convert the numbers to
hundreds_list = ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 
'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']

tens_list = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'nintety']

ones_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

other_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
'eighteen', 'nineteen']

#ensures we use the correct list for the entered number
if num < 10:
    print(ones_list[ones_digit])
elif num >= 10 and num <= 19:
    print(other_list[ones_digit])
elif num >= 20 and ones_digit != 0 and num < 100:
    print(f'{tens_list[tens_digit]}-{ones_list[ones_digit]}')
elif num >= 20 and ones_digit == 0 and num < 100:
    print(tens_list[tens_digit])
elif num > 99 and tens_digit == 0 and ones_digit == 0:
    print(hundreds_list[hundreds_digit])
elif num > 99 and tens_digit == 0:
    print(f'{hundreds_list[hundreds_digit]} and {ones_list[ones_digit]}')
elif num > 99 and tens_digit == 1:
    print(f'{hundreds_list[hundreds_digit]} and {other_list[ones_digit]}')
elif num > 99 and tens_digit >1 and ones_digit == 0:
    print(f'{hundreds_list[hundreds_digit]} and {tens_list[tens_digit]}')
else:
    print(f'{hundreds_list[hundreds_digit]} and {tens_list[tens_digit]}-{ones_list[ones_digit]}')
