cards = {
    'A': 1,
    'K': 10,
    'Q': 10,
    'J': 10,
}

card1 = input('What is your first card?\n>').upper()
card2 = input('What is your second card?\n>').upper()
card3 = input('What is your third card?\n>').upper()

if card1 in cards:
    card1 = int(cards[card1])
if card2 in cards:
    card2 = int(cards[card2])
if card3 in cards:
    card3 = int(cards[card3])

total = int(card1) + int(card2) + int(card3)

if total < 17:
    print(f'{total} - Hit')
if total in range(17,21):
    print(f'{total} - Stay')
if total == 21:
    print(f'{total} - Blackjack!')
if total > 21:
    print(f'{total} - Busted!')
