# Welcome to lab09 by Quinton Baseman

import random
# adding 6 random numbers to winning ticket list
winning_ticket = []
for i in range(6):
    winning_ticket.append(random.randint(1, 99))

# function to create each ticket with 6 random numbers
def my_ticket():
    my_list = []
    for i in range(6):
        my_list.append(random.randint(1, 99))
    return my_list

# function to check similarities in the winning ticket and my ticket, adding up the
# similarities and storing them in count
def check(blah, blah2):
    count = 0
    for i in range(6):
        if blah[i] == blah2[i]:
            count += 1
    return count

money_spent = 0
earnings = 0
# if else loop checking same numbers between my ticket and winning ticket using the 
# check function while adding corresponding amount to earnings.
while money_spent < 200000:
    money_spent += 2
    if check(my_ticket(), winning_ticket) == 1:
        earnings += 4
    elif check(my_ticket(), winning_ticket) == 2:
        earnings += 7
    elif check(my_ticket(), winning_ticket) == 3:
        earnings += 100
    elif check(my_ticket(), winning_ticket) == 4:
        earnings += 50000
    elif check(my_ticket(), winning_ticket) == 5:
        earnings += 1000000
    elif check(my_ticket(), winning_ticket) == 6:
        earnings += 25000000

# determining if you made or lost money, then printing out the final message
print(f'''
You spent: ${money_spent}
You won: ${earnings}''')

if money_spent > earnings:
    print(f'You lost: ${money_spent - earnings}')
else:
    print(f'You made: ${earnings - money_spent}')