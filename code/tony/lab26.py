import math

class player:
    def __init__(self, player, letter):
        self.player = player
        self.letter = letter
    def __repr__(self):
        return f'{self.player} is {self.letter}s'

class game:
    def __init__(self):
        self.moves = 0
        self.row1 = ['_', '|', '_', '|', '_']
        self.row2 = ['_', '|', '_', '|', '_']
        self.row3 = [' ', '|', '_', '|', ' ',]
            # 1 = row1[1] 2 = row1[2] 3 = row1[3]
            # 4 = row2[1] 5 = row1[2] 6 = row1[3]
            # 7 = row3[1] 8 = row1[2] 9 = row1[3]

    def move(self, x, y, letter):
        if x < 4:
            self.row1[y] = letter
        elif x > 3 and x < 7:
            self.row2[y] = letter
        elif x > 7 and < 10:
            self.row3[y] = letter
        
    def is_full():
        if self.moves == 9:
            return True
        else:
            return False

    def is_game_over():
        if game.isfull() == True or game.calc_winner() == True:
            return True
        else:
            return False

    # def __repr__(self):
    #     return f'{self.
p1 = player('Player 1', 'X')
p2 = player('Player 2', 'O')
start = game()
game_over = False
for x in range(15):
    if x % 5 == 0:
        print('\n')
    print(game.board[x], end=' ')

while game_over == False: