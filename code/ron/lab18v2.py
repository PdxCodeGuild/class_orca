

# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab18
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-16-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 18: Peaks and Valleys (ver. 1 & 2)

'''
#----Modules----------------------------------------------------

import string
import math
import random

#----Global variables, lists, dictionaries----------------------

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9] 
row = []

#----Functions--------------------------------------------------

def peaks(data):
    results = []
    for x in range(len(data)):  
        if x > 0 and x < len(data)-1:
            if data[x-1] < data[x] > data[x+1]:
                results.append(x)
    return results    

def valleys(data):
    results = []
    for x in range(len(data)):  
        if x > 0 and x < len(data)-1:
            if data[x-1] > data[x] < data[x+1]:
                results.append(x)
    return results   

def peaks_and_valleys(data):
    x1 = peaks(data)
    x2 = valleys(data)
    return x1 + x2

def count_row(data, count):
    for y in data:
        if y < count:
            row.append(' ')
        else: 
            row.append("x")
    return row

#----Main------------------------------------------------------

def main():

    print(f'\nDataset: {data}\n')

    print(f'Peak:   {peaks(data)}')
    print(f'Valley: {valleys(data)}')
    print(f'Both:   {peaks_and_valleys(data)}')

    for x in range(10, 0, -1):
        result = count_row(data, x)
        x = " ".join(result)
        print(x)
        row.clear()

    print(f'\n')

main()




