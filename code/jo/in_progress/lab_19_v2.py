
""" 
changes to make:
turn generate hand block into function
add option to hit 
generate computer hand
computer AI
"""

import random

# dictionary assigning values to cards
values = {"A": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"J": 10,"Q": 10,"K": 10}


#  loops through values of all your cards in hand and combine
def value_check():
    hand_count = 0
    hand_value = 0
    for cards in your_hand:
        card_value = values[your_hand[hand_count]] 
        hand_count += 1
        hand_value += card_value
    return hand_value

# turns dict into list then builds your hand by appending list with random card from dict
card = list(values)
your_hand = []
for i in range(3):
    your_hand.append(random.choice(card))

print(value_check())







""" # checks the total value against some comparisons to determine best advice
if total_value < 17:
    action = 'You should hit.'
elif 17 <= total_value <= 20:
    action = 'You should stay.'
elif total_value == 21:
    action = 'You got Blackjack!'
else:
    action = 'You\'re already busted'

# prints out the total value and advice
print (f"Your total value is {total_value}. {action}")
 """