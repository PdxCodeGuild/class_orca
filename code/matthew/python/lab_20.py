numbers = []
digits = []

# Ask the user for their CC number
cc_number = input("Please enter your credit card number ")
# assign that input to a list
numbers = list(cc_number)

# Convert the input string into a list of ints
for number in numbers:
    digits.append(int(number))

first_15 = digits[0:15]
# Slice off the last digit. That is the check digit.
check_digit = digits[15:16]
check_digit = check_digit[0]
# Reverse the digits.
reverse_digits = first_15[::-1]
# Double every other element in the reversed list.
double_reverse = [x * 2 for x in reverse_digits[::2]]
# Make a list for the numbers left out of the double reverse
the_others = reverse_digits[1::2]
# combine the two lists together
joined_list = double_reverse + the_others
#Subtract nine from numbers over nine.
subtract_9 = [x-9 if x > 9 else x for x in joined_list]
# Sum all values
sum = sum(subtract_9)
# Take the second digit of that sum
second_digit = sum % 10
# if check digit matches sum print valid
if second_digit == check_digit:
    print("Valid!")
else:
    print("Not valid")



#Testing Prints to check work
# print(f'CC Number {cc_number}')
# print(f'Reverse: {reverse_digits}')
# print(f'Double Reverse: {double_reverse}')
# print(f'The others: {the_others}')
# print(f'Joined List: {joined_list}')
# print(f'Subtract9: {subtract_9}')
# print(second_digit)
# print(f'Sum: {sum}')
# print(f'Second Digit: {second_digit}')
# print(f'Check Digit:{check_digit}')

#4556737586899855



