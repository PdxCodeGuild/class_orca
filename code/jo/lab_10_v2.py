# # Version 2
# #--------------------------------------

# an empty list to add to
num = []

# adds user input to the list
add_num = input('Enter a number to add it to the list and type "done" when finished ')

# loop to keep asking for input until entering done
while add_num != 'done':
    num.append(add_num)
    add_num = input('Enter a number to add it to the list and type "done" when finished ')

# prints out the new list
else:
    print(f'Your list is {num}')

# establishes a variable of zero to add values of list to
total = 0

 # for each item in list, will continue to add them to each other to get a total
for i in range(len(num)):
    total += int(num[i])

# divide the sum of all numbers by the number if items in the list to get the avearage
average = total / len(num)

# print it out
print(f'The average of the list is {average}')