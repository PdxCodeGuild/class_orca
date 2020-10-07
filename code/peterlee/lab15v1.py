num = int(input('enter a number from 0-99: '))

#separates the digits to ensure we can convert both into words
tens_digit = num//10
ones_digit = num%10

#creates lists of prefixes, suffixes, and standalone words that we can convert the numbers to
tens_list = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'nintety']

ones_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

other_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
'eighteen', 'nineteen']

#ensures we use the correct list for the entered number
if num < 10:
    print(ones_list[ones_digit])
elif num >= 10 and num <= 19:
    print(other_list[ones_digit])
elif num >= 20 and ones_digit != 0:
    print(f'{tens_list[tens_digit]}-{ones_list[ones_digit]}')
else:
    print(tens_list[tens_digit])