#This is Lab 19 Version 2 with changing aces

def main():
    def b_j_a(x):
        if x < 17:
            return "\nHit!"
        if 17 < x < 21:
            return "\nStay!"
        if x == 21:
            return "\nBlackjack! You lucky S.O.B."
        if x > 21:
            return "\nYou busted! Time to find an ATM"
    deck = {"J":10,
    "Q":10,
    "K":10,
    "A":11,
    "A2":1,
    "10":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2}
    card_1 = input("What is your first card: A, K, Q, J or 1 - 10?\n") 
    
    if card_1 not in deck:
        while card_1 not in deck:
            print ("What kind of deck is this? Try Again.\n")
            card_1 = input("What is your first card: A, K, Q, J or 1 - 10?\n")
    if card_1 in deck:
        card_1 = deck[card_1]
    
    card_2 = input("What is your second card: A, K, Q, J or 1 - 10?\n") 
    
    if card_2 not in deck:
        while card_2 not in deck:
            print ("What kind of deck is this? Try Again.\n")
            card_2 = input("What is your second card: A, K, Q, J or 1 - 10?\n")
    if card_2 in deck:
        card_2 = deck[card_2]
    
    card_3 = input("What is your third card: A, K, Q, J or 1 - 10?\n") 
    
    if card_3 not in deck:
        while card_3 not in deck:
            print ("What kind of deck is this? Try Again.\n")
            card_3 = input("What is your second card: A, K, Q, J or 1 - 10?\n")
    if card_3 in deck:
        card_3 = deck[card_3]
    x = (card_1 + card_2 + card_3)
    
    if x > 21:
        if card_1 == deck["A"] and card_2 == deck["A"] and card_3 == deck["A"]:
           x -= 20
        if card_1 == deck["A"] and card_2 == deck["A"] and card_3 != deck["A"]\
        or card_1 == deck["A"] and card_3 == deck["A"] and card_2 != deck["A"]\
        or card_2 == deck["A"] and card_3 == deck["A"] and card_1 != deck["A"]:
            if (x - 11) <= 21:
                x -= 10
            if (x -11) > 21:
                x -= 20
        if card_1 == deck["A"] or card_2 == deck["A"] or card_3 == deck["A"]:
            x -= 10



    print(f"You have {x}!\n {b_j_a(x)}")

main()