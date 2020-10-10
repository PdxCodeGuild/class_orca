
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
# Assignment/Ver: Lab20
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-09-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 
Lab 20: Credit Card Validaton
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

    print('\n  ** Credit Card Checker ** \n')

    # Random # generator
    cc_num = [random.randint(1,9) for x in range(16)]
    cc = [str(x) for x in cc_num]
    cc = ''.join(cc)
    print(f'Credit Card #: {cc}')

    # Find, store, and delete check digit
    check_digit = cc_num[len(cc_num) - 1]
    del cc_num[len(cc_num) - 1]
    # print(2, cc_num) # Error Check

    # Reverse numbers
    cc_num.reverse()
    # print(3, cc_num) # Error Check

    # Double the values of every other number
    cc_num = [cc_num[x] * 2 if x % 2 == 0 else cc_num[x] for x in range(len(cc_num))]
    # print(4, cc_num) # Error Check

    # Subtract 9 from every value
    cc_num = [cc_num[x] - 9 if cc_num[x] >= 9 else cc_num[x] for x in range(len(cc_num))]
    # print(5, cc_num) # Error Check

    # Output
    print(f'Total: {sum(cc_num)}')
    print(f'Checksum: {check_digit}')
    if sum(cc_num)%10 == check_digit:
        print(f'Status: {"Valid Card"}\n')
    else: 
        print(f'Status: {"Invalid Card"}\n')

main()

#--------End Code-------------------------------------------
