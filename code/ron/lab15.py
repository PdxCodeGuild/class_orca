
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
# Assignment/Ver: Lab15
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-07-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 15: Number to Phrase

'''
#----Modules------------------------------------------------

''' none '''

#----Global variables, lists, dictionaries------------------

num_conv = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    100 : "hundred",
}

#----Functions----------------------------------------------

def zero_19(num):
    for x, y in num_conv.items():
        if num == x:
            return y

def nineteen_99(num):
    ten_digit = (num//10)*10
    for x, y in num_conv.items():
        if ten_digit == x:
            return y

def hundred_999(num):
    hundred_digit = (num//100) #*100
    for x, y in num_conv.items():
        if hundred_digit == x:
            return y

#--------Main Code---------------------------------------------

def main():

    print('\nNumber conversion integer -> alphanumerics\n')
    user_input = input('Enter an integer: ')
    num = int(user_input)

    # 0-19
    if num > 0 and num < 20: 
        ones = zero_19(num)
        print(ones)

    # 20-99
    if num > 19 and num < 100:
        tens = nineteen_99(num)
        if num%10 > 0:
            ones = zero_19(num%10)
            print(f'{tens} {ones}')
        else:
            print (f'{tens}')

    # 100-999
    if num > 99 and num < 1000:
        hundreds = hundred_999(num) + " hundred"
        if num%100 == 0:
            print(hundreds)
        elif num%100 < 20:
            num1 = num - ((num//100)*100)
            ones = zero_19(num1)
            print(f'{hundreds} and {ones}')
        else:
            tens = nineteen_99(num%100)
            if num%10 > 0:
                ones = zero_19(num%10)
                print(f'{hundreds} and {tens} {ones}')
            else:
                print (f'{hundreds} and {tens}')           

    if True:
        main()

main()
