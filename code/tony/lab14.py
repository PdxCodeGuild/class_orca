import random
win_ticket = []
play_ticket = []
picknumber = 6
Win = 0
N = 0
wallet = 0
cost = 2

tickets = 10

def pick(y,ticket):
    for x in range(y):
        x = random.randrange(1,100)
        ticket.append(str(x))
    return ticket

def matchmaker(N, Win):
    for x in range(picknumber):
        if win_ticket[x] == play_ticket[x]:
            N = N + 1
            Win = Win + 1
    # if N == 0:
    #         print('Sorry, no matches!')
    return N, Win

def prizes():
    monies = 0
    if N == 1:
        monies = 4
        # print('Won $4!')
    elif N == 2:
        monies = 7
        # print('Won $7!')
    elif N == 3:
        monies = 100
        # print('Won $100!')
    elif N == 4:
        monies = 50,000
        # print('Won $50,000!')
    elif N == 5:
        monies = 1,000,000
        # print('Won $1,000,000!')
    elif N == 6:
        monies = 25,000,000
        # print('Jackpot! You won $25,000,000')
    return monies

while tickets != 0:
    tickets = tickets - 1
    wallet = wallet - cost

    pick(picknumber, win_ticket)
    pick(picknumber, play_ticket)
    N = matchmaker(N, Win)
    monies = prizes()
    wallet = wallet + monies
    win_ticket.clear()
    play_ticket.clear()

print(Win)
print(wallet)