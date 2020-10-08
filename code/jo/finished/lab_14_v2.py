
# get random to make random lists
import random

# creates a list from specific range of numbers
def gen6():
    pick6 = []
    for i in range(6):
        pick6.append(random.randrange(100))
    return pick6

# generates and compares tickets to winning number and decides how much was won
def comp6():
    # generates a ticket then compares that ticket to winning number to find number of matches
    my_numbers = gen6()
    matches = 0
    number_place = 0
    winnings = 0
    for i in my_numbers:
        if my_numbers[number_place] == winning_numbers[number_place]:
            matches += 1
        number_place += 1

    # determines amount won from ticket based on number of matches
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

# generates the winning ticket number and prints
winning_numbers = gen6()
print(f"The winning numbers are: {winning_numbers}")

# establishes baselines of ticket cost and total win to be added to
ticket_cost = 0
win_total = 0
# makes 100,000 tickets and adds up cost of each ticket and total amount won
for i in range(100000):
    ticket_cost -= 2
    win_total += comp6()

# shows total won and total profit
print(f'You won ${win_total}. With the cost of tickets though, your end total was ${win_total + ticket_cost}!')

# shows ROI (return on investment)
print(f'Your return on investment is: {(win_total - ticket_cost) / ticket_cost}')


