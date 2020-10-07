##############################################################################
# John Fial, PDX Code Guild, 2020
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab11-simple_calculator.md
##############################################################################




















##############################################################################
# copied lab from programming 102 lab below, using loops and functions:
##############################################################################

# REPL calculator for + and -
# https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab2.md

def addition(number1, number2):
    '''Adds two numbers together, by pasing two numbers in. Would probably concatenate two strings.'''
    # addition_result = number1 + number2 # REMOVE 
    # print(f'REMOVE THIS LINE. The addition result is: {addition_result}') # REMOVE
    return number1 + number2

def subtraction(number1, number2):
    '''Subtracts the second number from the first.'''
    # subtraction_result = number1 - number2 # REMOVE
    # print(f'REMOVE THIS LINE. The subtraction result is: {subtraction_result}') # REMOVE
    return number1 - number2

def multiply(number1, number2):
    '''Multiplies two numbers together.'''
    # multiplication_result = number1 * number2 # REMOVE
    # print(f'REMOVE THIS LINE. The multiplication result is: {multiplication_result}') # REMOVE
    return number1 * number2

def divide(number1, number2):
    '''Divides one number by another.'''
    # division_result = number1 / number2 # REMOVE
    # print(f'REMOVE THIS LINE. The division result is: {division_result}') # REMOVE
    return number1 / number2

# main math function
def math():
    
    user_operand = input(
    '''
    What is your operation to perform? 
    Please input one of the following, without the quotes: "+", "-", "*", "/", or "done" : ''')

    # main loop starts
    while True:

        #i don't like having this segment twice...
        while user_operand not in ["+", "-", "*", "/", "done"]:
            print('Invalid selection!')
            user_operand = input(
        '''
        What is your operation to perform? 
        Please input one of the following, without the quotes: "+", "-", "*", "/", or "done" : ''')
                        
        if user_operand == "done":
            print('goodbye!')
            break

        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        num1 = float(num1)
        num2 = float(num2)

        if user_operand == "+":
            # print('+ running successfully')
            addition_result = addition(num1, num2)
            print(f'{num1} + {num2} = {addition_result}')
            #And I don't like having break with each line...could be cleaner
            break

        elif user_operand == "-":
            # print('- running successfully')
            subtraction_result = subtraction(num1, num2)
            print(f'{num1} - {num2} = {subtraction_result}')
            break

        elif user_operand == "*":
            multiplication_result = multiply(num1, num2)
            print(f'{num1} * {num2} = {multiplication_result}')
            break

        elif user_operand == "/":
            division_result = divide(num1, num2)
            print(f'{num1} / {num2} = {division_result}')
            break

        else:
            print('exiting through ''else'' WHY????')
            break


#run it!
math()