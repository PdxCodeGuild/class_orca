#Number to Phrase

#Version 2: 0-999

num = int(input("Please enter a number from 0-999 "))

def num_to_phrase(num):
    ones_digit = num % 10
    tens_digit = ((num % 100) - ones_digit) / 10
    hundreds_digit = ((num % 1000) - (tens_digit * 10) - ones_digit) / 100

    ones_string = ""
    tens_string = ""
    hundreds_string = ""

    #Get hundreds digit

    if hundreds_digit == 9:
        hundreds_string = "nine hundred"
    
    if hundreds_digit == 8:
        hundreds_string = "eight hundred"
    
    if hundreds_digit == 7:
        hundreds_string = "seven hundred"
    
    if hundreds_digit == 6:
        hundreds_string = "six hundred"
    
    if hundreds_digit == 5:
        hundreds_string = "five hundred"

    if hundreds_digit == 4:
        hundreds_string = "four hundred"
    
    if hundreds_digit == 3:
        hundreds_string = "three hundred"
    
    if hundreds_digit == 2:
        hundreds_string = "two hundred"
    
    if hundreds_digit == 1:
        hundreds_string = "one hundred"

    if hundreds_digit == None:
        hundreds_string = ""
    
    #Get tens digit

    if tens_digit == 9:
        tens_string = "ninety"
    
    if tens_digit == 8:
        tens_string = "eighty"
    
    if tens_digit == 7:
        tens_string = "seventy"
    
    if tens_digit == 6:
        tens_string = "sixty"
    
    if tens_digit == 5:
        tens_string = "fifty"

    if tens_digit == 4:
        tens_string = "forty"
    
    if tens_digit == 3:
        tens_string = "thirty"
    
    if tens_digit == 2:
        tens_string = "twenty"
    
    if tens_digit == 1 and ones_digit == 9:
        tens_string = "nineteen" 
    
    if tens_digit == 1 and ones_digit == 8:
        tens_string = "eighteen" 
    
    if tens_digit == 1 and ones_digit == 7:
        tens_string = "seventeen" 
    
    if tens_digit == 1 and ones_digit == 6:
        tens_string = "sixteen" 
    
    if tens_digit == 1 and ones_digit == 5:
        tens_string = "fifteen" 
    
    if tens_digit == 1 and ones_digit == 4:
        tens_string = "fourteen" 
    
    if tens_digit == 1 and ones_digit == 3:
        tens_string = "thirteen" 
    
    if tens_digit == 1 and ones_digit == 3:
        tens_string = "thirteen" 
    
    if tens_digit == 1 and ones_digit == 2:
        tens_string = "twelve" 
    
    if tens_digit == 1 and ones_digit == 1:
        tens_string = "eleven" 
    

#Get ones digit
    if ones_digit == 1 and tens_digit != 1:
        ones_string = "one"
    
    if ones_digit == 2 and tens_digit != 1:
        ones_string = "two"
    
    if ones_digit == 3 and tens_digit != 1:
        ones_string = "three"
    
    if ones_digit == 4 and tens_digit != 1:
        ones_string = "four"
    
    if ones_digit == 5 and tens_digit != 1:
        ones_string = "five"
    
    if ones_digit == 6 and tens_digit != 1:
        ones_string = "six"
    
    if ones_digit == 7 and tens_digit != 1:
        ones_string = "seven"

    if ones_digit == 8 and tens_digit != 1:
        ones_string = "eight"
    
    if ones_digit == 9 and tens_digit != 1:
        ones_string = "nine"
    
    if ones_digit == 0 and tens_digit != 1:
        ones_string = ""

    if ones_digit == 0 and tens_digit == False and hundreds_digit == False:
        ones_string = "zero"

    print(hundreds_string, tens_string, ones_string)

print(str(num_to_phrase(num)))