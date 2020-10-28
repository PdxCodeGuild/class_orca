##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab20-credit_card_validation.md
##############################################################################


def validate(input_card_number):

    # Welcome
    print('Welcome to Credit Card Validation v1.')
    print(f'Testing card #: {input_card_number}')

    #     Convert the input string into a list of ints
    test_card_list = [int(num) for num in input_card_number ]
        # Multiple line version of above single line 'Comprehension':
        # test_card_list = []
        # for num in input_card_number:
        #     test_card_list.append(int(num))
    print(f'Card as a list is {test_card_list}')


    #     Slice off the last digit. That is the check digit.
    # check_digit = test_card_list[-1] # WRONG, made a copy...want to pop...
    check_digit = test_card_list.pop(-1)
    print(f'Check digit is {check_digit} and new list is now {test_card_list}')


    #     Reverse the digits.
    test_card_list_reverse = test_card_list.copy()
    test_card_list_reverse.reverse()
    print(f'Reversed list is {test_card_list_reverse}')


    #     Double every other element in the reversed list.
    for index in range(len(test_card_list_reverse)):
        # print(f'Index is {index}.')
        if (index+1) % 2:
            temp = test_card_list_reverse[index]
            test_card_list_reverse.pop(index)
            test_card_list_reverse.insert(index, temp*2) # insert number
            # print(f'Temp number popped is {temp} at index {index}. New list is {test_card_list_reverse}') #very helpful line to see for loop
    print(f'Doubled list is {test_card_list_reverse}')


    #     Subtract nine from numbers over nine.
    for index in range(len(test_card_list_reverse)):
        if test_card_list_reverse[index] > 9:    
            temp = test_card_list_reverse[index]
            test_card_list_reverse.pop(index)
            test_card_list_reverse.insert(index,temp-9)
        else:
            pass
    print(f'New list, with -9 to all numbers>9, is {test_card_list_reverse}')


    #     Sum all values.
    sum = 0
    for num in test_card_list_reverse:
        sum += num
    print(f'Sum of list is {sum}')


    #     Take the second digit of that sum.
    sum = str(sum) # need to convert to a string to call
    digit_2 = sum[1] # remember first character is 0, second is 1...
    digit_2 = int(digit_2) # convert back...
    print(f'2nd digit is {digit_2}')


    #     If that matches the check digit, the whole card number is valid.
    if digit_2 == check_digit:
        print('**********PASSED VALIDATION!**********')
        print(f'Thank you!')
    else:
        print('**********FAILED VALIDATION!**********')
        print(f'Thank you!')



# input_card_number 
# run some checks to validate 16 digits, only numbers, no spaces, etc...
input_card_number = input('Please input your 16-digit card number, without spaces or other characters: ')

valid_card_1 = '4077247134350245' # PASSED!
valid_card_2 = '4281471859733607' # FAILED...
valid_card_3 = '4318214376804015' # PASSED!
valid_card_4 = '4527696733892419' # FAILED...


# run it!
validate(input_card_number)









# practice 5 'comprehensions' could give some practice first...
##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab20-credit_card_validation.md
##############################################################################
# Lab 20: Credit Card Validation

# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

#     Convert the input string into a list of ints
#     Slice off the last digit. That is the check digit.
#     Reverse the digits.
#     Double every other element in the reversed list.
#     Subtract nine from numbers over nine.
#     Sum all values.
#     Take the second digit of that sum.
#     If that matches the check digit, the whole card number is valid.

# For example, the worked out steps would be:

#     4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
#     4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
#     5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
#     10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
#     1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
#     85
#     5
#     Valid!