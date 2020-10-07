# This is lab 15 Version 1 "Number to Phrase Conversion"
def main():
    def number_to_word (x):
        x = int(x)
        teens = {11:"eleven",
        12:"twelve", 
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eightteen",
        19:"nineteen"}
        first_digit = {2:"twenty",
        3:"thirty",
        4:"forty",
        5:"fifty",
        6:"sixty",
        7:"seventy",
        8:"eighty",
        9:"ninety"}
        second_digit = {0:"zero",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten"}
        if x == 0:
            return second_digit[0]
        if x // 10 == 0:
            return second_digit[x]
        if x == 10:
            return second_digit[10]
        if 11<= x <= 19:
            return teens[x]
        if 20 <= x <= 99:
            return f"{first_digit[(x//10)]}-{second_digit[(x%10)]}" 
    x = input("enter a number between 1 and 99:\n")
    while int(x) not in range(0,99):
        print("No good. Try again...:\n")
        x = input("Enter a number between 1 and 99\n")
    print(f"{x} equals {number_to_word(x)}!")

main()