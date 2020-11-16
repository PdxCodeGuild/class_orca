'''
    PDX Code Guild
    Daniel Eggimann
    Lab10
'''

''' Version 1 '''

# list of numbers
nums = [5,0,8,3,4,1,6]
# running sum of nums
nums_average = 0
# for loop to run through each item in nums list
for num in nums:
    nums_average += num
# calculate the average of nums_average using len(nums)
nums_average = nums_average / len(nums)
# output
print(nums)
print(f'The average of the list of numbers is {nums_average:.2f}')

''' Version 2 '''

user_list = []
user_average = 0
user_input = input("Enter as many numbers as you would like,\none at a time, to find the average.\nWhen you have entered all of your numbers enter 'done'.\n>")
while user_input != 'done':
    user_input = int(user_input)
    user_list.append(user_input)
    user_average += user_input
    user_input = input("Enter as many numbers as you would like,\none at a time,to find the average.\nWhen you have entered all of your numbers enter 'done'.\n>")
if user_input == 'done':
    user_average = user_average / len(user_list)

print(f'The average of your list is {user_average:.2f}')