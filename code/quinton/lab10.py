nums = []
total = 0
# loop that gathers each number from the user
while True:
    number = input('enter a number, or \'done\': ')
    if number == 'done':
        break
    else:
        nums.append(number)
# looping through the list, adding the numbers to 
# the total, then dividing to get the average
for num in nums:
    total += int(num)
    average = int(total) / len(nums)
# printing out final
print(f'''
Your list:
{nums}

The added total of your list is {total}
The average of your list is {average}
''')