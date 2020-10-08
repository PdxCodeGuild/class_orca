#function that returns the value of current cards
def get_card(a):
    if a == 'J':
        return 10
    elif a == 'Q':
        return 10
    elif a == 'K':
        return 10
    elif a == 'A':
        return 1
    else:
        return int(a)

#asks the user for their current cards
card_one = input("What's your first card? ")
card_two = input("What's your second card? ")
card_three = input("What's your third card? ")

total = get_card(card_one) + get_card(card_two) + get_card(card_three)

#prints total and advice
if total < 17:
    print(f'{total} Hit')
elif total >=17 and total < 21:
    print(f'{total} Stay')
elif total == 21:
    print(f'{total} Blackjack!')
else:
    print(f'{total} Already Busted')