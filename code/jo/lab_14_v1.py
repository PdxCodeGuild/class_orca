import random

def gen6():
    pick6 = []
    for i in range(6):
        pick6.append(random.randrange(100))
    return pick6

def comp6():
    my_numbers = gen6()
    matches = 0
    number_place = 0
    winnings = 0
    for i in my_numbers:
        if my_numbers[number_place] == winning_numbers[number_place]:
            matches += 1
        number_place += 1

    if matches == 1:
        winnings = 4
    elif matches == 2:
        winnings = 7
    elif matches == 3:
        winnings - 100
    elif matches == 4:
        winnings = 50000
    elif matches == 5:
        winnings = 1000000
    elif matches == 6:
        winnings = 25000000
    elif matches == 0:
        winnings = 0
    return winnings

winning_numbers = gen6()
print(f"The winning numbers are: {winning_numbers}")

ticket_cost = 0
win_total = 0
for i in range(100000):
    ticket_cost -= 2
    win_total += comp6()

print(f'You won ${win_total}. With the cost of tickets though, your end total was ${win_total + ticket_cost}!')








    

