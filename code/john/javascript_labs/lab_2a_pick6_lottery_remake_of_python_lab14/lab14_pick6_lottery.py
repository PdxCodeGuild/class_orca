##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab14-pick6.md
##############################################################################

import random

# Define a function to pick 6 numbers between 1-99 and store them in a simple list:
def pick6(ticket_name):
    # COMPREHENSION: 
    # return [random.randint(1,99) for x in range(6)]
    while len(ticket_name) < 6:
        ticket_name.append(random.randint(1,99))
        # print(f'generating ticket: {ticket_name}')
    else:
        # print(f'ticket is: {ticket_name}')
        return ticket_name

# making the function to match how many numbers
def matching_numbers(winning_ticket, ticket):

    matching_number_total = 0

    for x in range(6):
        if ticket[x] == winning_ticket[x]:
            # print(f'matching_number_total is {matching_number_total}')
            matching_number_total += 1
            # print(f'matching_number_total is now {matching_number_total}')
    return matching_number_total

print('CURRENTLY USING LENIENT MATCHING NUMBERS ALGORITHM')
def matching_numbers_lenient(winning_ticket, ticket):

    matching_number_total = 0

    for num in ticket:
        if num in winning_ticket:
            matching_number_total += 1
        else:
            pass
    return matching_number_total

# Stored dictionary of how much money we earn with each matched number
winnings_dictionary = {
    # number matches : winnings in $ dollars
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000,
}

# create then store the winning ticket
winning_ticket = []
winning_ticket = pick6(winning_ticket)

# Welcome
print(f'Welcome to powerball lottery v1.0! The winning ticket is: {winning_ticket}.')

# Create new user balance
user_balance = 0
# print(f'Your balance is: ${user_balance}.')

# We don't want this defined within the loop, because it'd be overwritten (unless I make a loop?)
user_winnings_total = 0

# later I could make this an input...
tickets_purchased = 100000
print(f'You just purchased {tickets_purchased} tickets at $2 each, costing ${tickets_purchased*2}! Calculating your winnings and balance...')

# THIS COULD BE A FUNCTION...
# Here's where we go through all the tickets purchased and change the balance
for x in range(tickets_purchased):

    # Create a blank ticket and generate its ticket numbers    
    ticket = []
    pick6(ticket)

    # Compare their ticket to the winning ticket, storing the number of matching numbers...
    matching_numbers_total = matching_numbers(winning_ticket, ticket)

    # ... and comparing the number to the winnings dictionary.
    user_winnings = winnings_dictionary.get(matching_numbers_total)
    # if user_winnings > 0:
    #     print(f'You earned ${user_winnings}!')
    # else:
    #     pass

    # Subtract ticket price, and add the user's winnings to their balance
    user_balance -= 2
    user_balance += user_winnings

    # Add their winnings to a total so we can tell thim just how much they won in total
    user_winnings_total += user_winnings

# The ROI (return on investment) is defined as (earnings - expenses)/expenses. 
ROI = (user_winnings_total - tickets_purchased * 2) / (tickets_purchased * 2)
print(f'''Financial Report:
    You earned a total of ${user_winnings_total}!
    Your final balance is: ${user_balance}. 
    Your return on investment was: {ROI}. Thanks for giving us your hard earned money!''')

# **************************************** WORKING FROM HERE *******************************
# ****************************************  TO HERE ****************************************