import random
winningnumbers = []
choices = []
check = 6
picknumber = 6
N = 0

def pick(y):
    for x in range(y):
        x = random.randrange(1,2)
        winningnumbers.append(str(x))
    return winningnumbers

# def player(y):
    # choices = input(f'Type {picknumber} numbers (1-99) ').replace(',',' ').split()
    # if len(choices) == y:
    #     return choices
    # else:
    #     print(f'Pick {picknumber} numbers!')
    #     choices.clear()
    #     return player(y)
    # return choices

def matchmaker(N):
    for x in range(picknumber):
        if winningnumbers[x] == p_num[x]:
            N = N+1
            print(f'Number {p_num[x]} matched!')
    if N == 0:
            print('Sorry, no matches!')
    return N

def prize():
    if N == 1:
        print('Won $4!')
    elif N == 2:
        print('Won $7!')
    elif N == 3:
        print('Won $100!')
    elif N == 4:
        print('Won $50,000!')
    elif N == 5:
        print('Won $1,000,000!')
    elif N == 6:
        print('Jackpot! You won $25,000,000')

# pick(picknumber)
# p_num = player(picknumber)
# N = matchmaker(N)
# prize()

# print(winningnumbers)
# print(p_num)