'''
Lab 14
Matthew Chimenti
version 1 and 2
'''

import random

counter = 0
ticket_counter = 0
matches = 0
spending = 0
winnings = 0
single_ticket = []


#ticket generator
def pick_6():
    ticket = []
    counter = 0
    while True:
        if counter < 7:
            counter += 1
            numbers = (random.randint(0, 99))
            ticket.append(numbers)
        else:
            return ticket
winning_ticket = pick_6()


for _ in range(100000):
    single_ticket = pick_6()
    matches = 0
    spending += - 2
    for i in range(6):
        if single_ticket[i] == winning_ticket[i]:
            matches += 1
    if matches == 1:
        winnings += 4
    elif matches == 2:
        winnings += 7
    elif matches == 3:
        winnings += 100
    elif matches == 4:
        winnings += 50000
    elif matches == 5:
        winnings += 1000000
    elif matches == 6:
        winnings += 25000000
    else:
        continue

number_tickets_bought = spending // -2
balance = spending + winnings
roi = (winnings - spending) / spending

print(f'Winnings: ${winnings}')
print(f'You bought {number_tickets_bought} tickets for $2 each, spending ${spending}, and won ${winnings}')
print(f'You have lost ${balance}')
print(f'You have a roi of{roi}')


