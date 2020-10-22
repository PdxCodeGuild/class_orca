import random

first_card = input("What is your first card?  ")

second_card = input("What is your second card?  ")

third_card = input("What is your third card?  ")

player_hand = [first_card, second_card, third_card]
counted_hand = []

for x in player_hand:
    if x in ('K','k','Q','q','J','j'):
        x = 10
        counted_hand.append(int(x))
    elif x in ('A','a'):
            x = 11
            counted_hand.append(int(x))
    else:
        counted_hand.append(int(x))

if 11 in counted_hand and sum(counted_hand) > 21:
    for i, x in enumerate(counted_hand):
        if sum(counted_hand) > 21 and x == 11:
            x = 1
            counted_hand[i] = int(x)

print(sum(counted_hand))

if sum(counted_hand) > 21:
    print('Bust')
elif sum(counted_hand) == 21:
    print('Blackjack!')
elif sum(counted_hand) >= 17:
    print('Stay!')
else:
    print('Hit!')