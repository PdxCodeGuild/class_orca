
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab19
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-07-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 19: Blackjack Advice

'''
#----Modules------------------------------------------------

import math
import string

#----Global variables, lists, dictionaries------------------

''' None '''

#----Functions----------------------------------------------

def hand_eval(hand):
    if sum(hand) < 17:
        return ('Hit')
    elif sum(hand) > 16 and sum(hand) < 21:
        return ('Stay')
    elif sum(hand) == 21:
        return ('Blackjack!')
    elif sum(hand) > 21:
        return ('Busted')
    else:
        return ('Invalid Selection')
        
#--------Main Code---------------------------------------------

def main():
 
    hand = []

    # Input
    hand.append(input('First card: ').capitalize())
    hand.append(input('Second card: ').capitalize())
    hand.append(input('Third card: ').capitalize())

    # Assign value to J, Q, K, A
    for y in range(0, len(hand)):
        if hand[y] == ("Q" or "K" or "J"):
            hand[y] = 10
        elif hand[y] == ("A"):
            hand[y] = 11

    # Str -> Int
    for y in range(0, len(hand)): 
        hand[y] = int(hand[y])

    # Hand evaluation function and output
    recommendation = hand_eval(hand)
    print(f'{sum(hand)} {recommendation}')

main()







