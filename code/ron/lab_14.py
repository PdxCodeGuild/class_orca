

# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
# Assignment/Ver: Lab14
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-08-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 14: Pick 6
'''
#----Modules------------------------------------------------

import math
import string
import random

#----Global variables, lists, dictionaries------------------

# Left over for future development
# match = {
#     1 : 4,
#     2 : 7,
#     3 : 100,
#     4 : 50000,
#     5 : 1000000,
#     6 : 25000000,
# }

#----Functions----------------------------------------------

def random_ticket_nums():
    ''' Random ticket generator '''
    x = 1
    ticket = []
    while x <= 6:
        ticket.append(random.randint(1,99))
        x += 1
    return ticket

def num_match(matches):
    ''' Checking # matches, assigning price money '''
    prize = 0
    if matches == 1:
        prize += 2
    if matches == 2:
        prize += 7
    if matches == 3:
        prize += 100   
    if matches == 4:
        prize += 50000
    if matches == 5:
        prize += 1000000   
    if matches == 6:
        prize += 2500000
    return prize

#--------Main Code------------------------------------------

def main():

    matches = 0
    money_spent = 0
    prize_money = 0

    for y in range(0, 100000):
        # Building tickets, setting paramters
        my_ticket = random_ticket_nums()
        winning_ticket = random_ticket_nums()
        matches = 0
        money_spent += 2

        # Checking tickets for matches and tallying prizes
        for x in range(0,6):
            if my_ticket[x] == winning_ticket[x]:
                matches += 1
                if matches > 0:
                    prize_money += num_match(matches)

    # Output
    roi = (prize_money - money_spent)/money_spent 
    print(f'\nInvestment: {money_spent}')
    print(f'Prize Money: {prize_money}')
    print(f'Net Income: {prize_money - money_spent}')
    print(f'ROI: {roi:.2f}\n')

main()
























#--------End Code-------------------------------------------
