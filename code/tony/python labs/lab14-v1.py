import random
numbers = []
winningnumbers = []
playerticket = []
check = 6
picknumber = 6
tickets = 10
starting_tickets = tickets
wins = 0
wallet = 0
winnings = 0

def pick(y,lister):
    for x in range(y):
        x = random.randrange(1,10)
        lister.append(str(x))
    return lister


def matchmaker(wins):
    for x in range(picknumber):
        if winningnumbers[x] == playerticket[x]:
            wins = wins+1
            # print(f'Number {playerticket[x]} matched!')
    # if wins == 0:
    #         print('Sorry, no matches!')
    return wins

def prize(winnings):
    if wins == 1:
        winnings += 4
        # print('Won $4!')
    elif wins == 2:
        winnings += 7
        # print('Won $7!')
    elif wins == 3:
        winnings += 100
        # print('Won $100!')
    elif wins == 4:
        winnings += 50000
        # print('Won $50,000!')
    elif wins == 5:
        winnings += 1000000
        # print('Won $1,000,000!')
    elif wins == 6:
        winnings += 25000000
        # print('Jackpot! You won $25,000,000')
    return winnings

while tickets != 0:
    tickets -= 1
    wallet -= 2
    winningnumbers = pick(picknumber,winningnumbers)
    playerticket = pick(picknumber,playerticket)
    wins = matchmaker(wins)
    # print(f'{wins} 1st check')
    winningnumbers.clear()
    playerticket.clear()
    wallet = prize(wallet)
    winnings = prize(winnings)
    wins = 0
    # print(f'wins cleared')
print(f'You spent ${starting_tickets*2} on {starting_tickets} tickets, and won ${winnings}.')
print(f'You ended with up ${wallet}!')