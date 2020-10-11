# Welcome to lab20 by Quinton Baseman

x = input('Please enter 16 digit card number. No spaces.\n>')
num_list = []
#step 1: Convert the input string into a list of ints
for i in x:
    num_list.append(int(i))
#step 2: Slice off the last digit assign it to variable check_digit
check_digit = num_list.pop(-1)
#step 3: Reverse the digits
num_list.reverse()
#step 4: Double every other element in the reversed list
doubled_list = num_list[:]
doubled_list[::2] = [item*2 for item in doubled_list[::2]]
#step 5: Subtract nine from numbers over nine
minus_9 = [x - 9 if x > 9 else x for x in doubled_list]
#step 6: Sum all values
sum = 0
for i in minus_9:
    sum += i
#step 7: Take the second digit of that sum
if sum >= 10:
    final = sum % 10
else:
    final = sum
#step 8: compare final number to check digit
if final == check_digit:
    print('This card number checks out. Valid!')
else:
    print('This card number does NOT check out. Invalid!')

#4556737586899855 returns Valid
#4318214376802398 return Invalid