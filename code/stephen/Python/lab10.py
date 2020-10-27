# LAB 10

# VERSION 1

'''
nums = [5, 0, 8, 3, 4, 1, 6]
total = 0
for number in range(0, len(nums)):
    total = total + nums[number]
    avg = total / len(nums)
print(f'Your average number of all listed numbers is {avg:.0f}.')
'''


# VERSION 2














nums = []
done = False
while done == False:
    user_num = input('Enter in a number or type done to get your average of input numbers: ')
    if user_num == 'done':
        done = True
    else: 
        user_num = int(user_num)
        nums.append(user_num)

total = 0
for number in nums:
    total = total + number

avg = total / len(nums)

print(f'The average for all numbers inputted is {avg}!') 