##############################################################################
# John Fial, PDX Code Guild, 2020
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab10-average_numbers.md
# Lab 10: Average Numbers
##############################################################################

nums = []
user_input = input('Enter a single number, or "done" when done to return the average: ')
user_input = float(user_input)
numbers_sum = 0

while user_input != 'done':
    user_input = float(user_input)
    nums.append(user_input)
    numbers_sum += user_input
    # print(nums) # REMOVE
    user_input = input('Enter another, or "done" when done to return the average: ')
    continue
else:
    # print(nums) # REMOVE
    print(f'There are {len(nums)} numbers in the list {nums}.') # REMOVE
    print(f'The sum total is {numbers_sum}.') # REMOVE
    average = numbers_sum / len(nums)
    print(f'The average of the list is {average}.')
    # print('WHILE LOOP TERMINATION') # REMOVE


# PSEUDOCODE:
# # # ask for user input
# add user input to sum of numbers
# # # when user input == done,...
# get length of list with len(nums)
# divide by length of list!