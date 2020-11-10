'''
PDX Code Guild
Daniel Eggimann
Lab_19 Version_1
'''
# imports
import random
import time 

# the full deck of cards
deck = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J' ,'Q', 'K',
'A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J' ,'Q', 'K',
'A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J' ,'Q', 'K',
'A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J' ,'Q', 'K']

def draw_hand():
    # drawing three random cards 
    hand = []
    count = 0
    while count <= 2:
        count += 1
        hand.append(str(random.choice(deck)))
    return hand
 
def point_value(cards):
    # determine point value
    value = 0
    for card in cards:
        if card.isalpha():
            if card == "A":
                value += 1
            if card in ['J', 'Q', 'K']:
                value += 10
        if card.isnumeric():
            card = int(card)
            value += card
    return value

def analyze_value(value):
    if value < 17:
        advice = "You should hit."
    elif 17 <= value <= 21:
        advice = "You should stay."
    elif value == 21:
        advice = "You got blackjack!"
    elif value > 21:
        advice = "You busted!"
    return advice 

def main():
    hand = draw_hand()
    points = point_value(hand)
    advice = analyze_value(points)
    hand = ', '.join(hand)
    print(f'You were dealt: {hand}.')
    print(f'Your hand is worth: {points} points.')
    time.sleep(1.5)
    print(advice)

main()


