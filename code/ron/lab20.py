

# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
# Assignment/Ver: Lab20
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-09-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 20: Credit Card Validaton


x I Convert the input string into a list of ints
x II Slice off the last digit. That is the check digit.
x III Reverse the digits.
x IV Double every other element in the reversed list.
x V Subtract nine from numbers over nine.
x VI Sum all values.
x VII Take the second digit of that sum.
x VIII If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

I 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
II 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
III 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
IV 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
V 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
VI 85
VII 5
VIII Valid!

'''
#----Modules------------------------------------------------

import math
import string
import random

#----Global variables, lists, dictionaries------------------

''' None '''

#----Functions----------------------------------------------

''' None '''

#--------Main Code------------------------------------------

def main():

    # Random # generator
    cc_num = [random.randint(1,9) for x in range(16)]
    print(1, cc_num) # Error Check

    # Convert to str
    cc_num = [str(num) for num in cc_num]
    print(2, cc_num) # Error Check

    # Convert to int
    cc_num = [int(num) for num in cc_num]
    print(3, cc_num) # Error Check

    # Find and store check digit
    check_digit = cc_num[len(cc_num) - 1]
    print(4, check_digit) # Error Check

    # Delete check digit
    del cc_num[len(cc_num) - 1]
    print(5, cc_num) # Error Check

    # Reverse numbers
    cc_num.reverse()
    print(6, cc_num) # Error Check

    # Double the values of every other number
    cc_num = [cc_num[x] * 2 if x % 2 == 0 else cc_num[x] for x in range(len(cc_num))]
    print(7, cc_num) # Error Check

    # Subtract 9 from every value
    cc_num = [cc_num[x] - 9 if cc_num[x] >= 9 else cc_num[x] for x in range(len(cc_num))]
    print(8, cc_num) # Error Check

    # Output
    print(f'Total: {sum(cc_num)}')
    print(f'Checksum: {check_digit}')
    if sum(cc_num)%10 == check_digit:
        print('Valid')
    else: 
        print('Invalid\n')

main()



#--------End Code-------------------------------------------






''' Excess, left over code ----------------------------------------'''

# Delete check digit
# cc_num = [del cc_num[x] for x in cc_num if check_digit == x]

# Reverse numbers
# reverse = [cc_num[x] for x in cc_num]

   # # Double the values of every other number
    # for index in range(len(cc_num)): 
    #     if index % 2 == 0:
    #         cc_num[index] = cc_num[index] * 2
    # print(7, cc_num) # Error Check


    # Subtract 9 from every value
    # for index in range(len(cc_num)):
    #         if cc_num[index] >= 9:
    #             cc_num[index] = cc_num[index] - 9

# # Double every other element (gotta be a better way to do this)
# cc_num = cc_num[0::2]
# print(cc_num) # Error Check
# cc_num = [cc_num[0::2]*2 for value in cc_num]
# print(cc_num) # Error Check

# for x in range(len(cc_num) - 1)
#     if cc_num[x]








#--------End Code-------------------------------------------
