'''
Lab 15
Version 1
Matthew Chimenti
'''

units = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
]

digits = [
    "", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
]

hundreds = [
    "none", "one-hundred", "two-hundred", "tree-hundred", "four-hundred", "five-hundred", "six-hundred",
    "seven-hundred", "eight-hundred", "nine-hundred"
]

conversion = int(input("enter a number "))
if conversion < 20:
    print(units[conversion])

elif conversion >= 20 < 100:
    number = conversion % 10
    digit = conversion % 100 // 10
    hundred = conversion // 100
    print(f'{hundreds[hundred]} {digits[digit]} {units[number]}')




