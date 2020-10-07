

# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab10
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-03-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes--------------------------------
''' 

Unit Converter

'''
#----Modules------------------------------------------------

''' none '''

#----Global variables, lists, dictionaries------------------

nums = [5, 0, 8, 3, 4, 1, 6]
x = 0

#----Functions----------------------------------------------

''' none '''

#----Main Code---------------------------------------------


''' Version 1 '''
print("\nVersion 1")
print("----------\n")

# Loop over the elements and add ** Some code copied from lab
for num in nums:
    x += num

# Calculate and output
y = x / len(nums)
print(f'{y:.2f}')


''' Version 2 '''
print("\nVersion 2")
print("----------\n")

num_list = []


# Input loop
while True:
    user_input = input('Enter a number, or done: ') 
    if user_input == 'done':
        # Calculate the average and return value
        for num in nums:
            x += num
        y = x / len(nums)
        print(f'\n ** Average is {y:.2f} **\n')
        exit()
    else:
        # Build list with values
        user_input = int(user_input)
        num_list.append(user_input)


#----End Code----------------------------------------------


