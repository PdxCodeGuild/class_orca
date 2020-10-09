
cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
hand = []


def sum_of_your_cards():
    total = 0
    for i in hand:
        total += i
    print(total)

    if total < 17:
        print('hit')
    elif total >= 17 and total < 21:
        print('stay')
    elif total == 21:
        print('Blackjack!')
    else:
        print("already busted")


card1 = input("What's your first card? ")
if card1 in ['j', 'q', 'k']:
    card1 = 10
    hand.append(card1)

elif card1 in ['a']:
    card1 = 1
    hand.append(card1)
else:
    card1 = int(card1)
    hand.append(card1)


card2 = input("What's your second card? ")
if card2 in ['j', 'q', 'k']:
    card2 = 10
    hand.append(card2)
elif card2 in ['a']:
    card2 = 1
    hand.append(card2)
else:
    card2 = int(card2)
    hand.append(card2)


card3 = input("What's your third card? ")
if card3 in ['j', 'q', 'k']:
    card3 = 10
    hand.append(card3)
elif card3 in ['a']:
    card3 = 1
    hand.append(card3)
else:
    card3 = int(card3)
    hand.append(card3)

sum_of_your_cards()
