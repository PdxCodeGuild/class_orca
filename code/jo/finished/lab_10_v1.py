# Version 1
# --------------------------------------

# the list of numbers
num = [45, 34, 86, 77, 22, 98, 56, 44]

#establish a variable to add to
total = 0

# for each item in list, will continue to add them to each other to get a total
for i in range(len(num)):
    total += num[i]

# divide the sum of all numbers by the number if items in the list to get the avearage
average = total / len(num)

# print it out
print(f'The average of the list is {average}')



