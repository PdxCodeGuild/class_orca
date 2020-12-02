card_value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'K': 10, 'Q': 10}

while True:
    card1 = input("Please enter your first card ")
    card2 = input("Please enter your second card ")
    card3 = input("Please enter your third card ")
    break

def get_value(card):
    if card_value[card]:
        return card_value[card]

def vegas_baby(card1, card2, card3):
    total = get_value(card1) + get_value(card2) + get_value(card3)
    print(total)

    if total < 17:
        print("Hit")

    if total >= 17 and total < 21:
        print("Stay")
    
    if total == 21:
        print("Blackjack!")
    
    if total > 21:
        print("Already busted")


print(vegas_baby(card1, card2, card3))

