
""" 
changes to make:
turn generate hand block into function
work on option to hit 
generate computer hand
computer AI
fix aces
"""

import random

# dictionary assigning values to cards
values = {"A": 11,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"J": 10,"Q": 10,"K": 10}


#  loops through values of all your cards in hand and combine
def value():
    hand_count = 0
    hand_value = 0
    global your_hand
    for cards in your_hand:
        card_value = values[your_hand[hand_count]] 
        hand_count += 1
        hand_value += card_value
        # for ace in hand, if hand_value > 21, subtract 9 from total
        for card in your_hand:
            if hand_value > 21:
                if card == "A":
                    hand_value = hand_value - 10
    return hand_value

# suggests action based on hand value
def value_check():
    if value() < 17:
        action = 'You should hit.'
    elif 17 <= value() <= 20:
        action = 'You should stay.'
    elif value() == 21:
        action = 'You got Blackjack!'
    else:
        action = 'You\'re already busted'
    return action

# turns dict into list then builds your hand by appending list with random card from dict
card = list(values)
your_hand = []
for i in range(3):
    your_hand.append(random.choice(card))

# prints your hand and hand value    
print(f"Your opening hand is {your_hand} giving you a value of {value()}")

# prints a suggestion
print(value_check())

# asks if you want to hit or not. if yes, gives you another card, new hand total, and new suggestion
hit = input("Would you like to hit? (y/n) ")
while hit == "y":
    your_hand.append(random.choice(card))
    print(f"Your hand is now {your_hand} giving you a value of {value()}")
    print(value_check())
    hit = input("Would you like to hit? (y/n) ")
if hit == "n":
    print('okay')





