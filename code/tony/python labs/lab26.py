import math
board_in = {
     1: {'left': 'x', 'center': 'x', 'right': 'x'},
     2: {'left': 'x', 'center': ' ', 'right': 'o'},
     3: {'left': 'x', 'center': ' ', 'right': 'x'}
}
row_names = ['Top','top','middle','Middle','Bottom','bottom']
column_names = ['Left','left','Center','center','Right','right']

class player:
    def __init__(self, player, letter):
        self.player = player
        self.letter = letter
    def __repr__(self):
        return f'{self.player} is {self.letter}s'

class game:
    def __init__(self):
        self.moves = 0
    
    def turn(self, p1, p2):
        if next_turn == p2:
            return p1
        else:
            return p2

    def move(self, row, column, letter):
        self.moves += 1
        rows = {'top': 1, 'middle': 2, 'bottom':3}
        self.row = rows[row]
        self.column = column
        if board_in[self.row][self.column] is ' ':
            board_in[self.row][self.column] = letter
            space = True
            return space
        else:
            space = False
            print('Space taken! Try again.')
            return space
 
    # def calc_winner(self):
    #     for x in range(3):
            # if all(y == ('x' or 'o') for y in board_in[x].values()):
            #     return y
            # elif all(y == ('x' or 'o') for y in board_in[x].values()):

    def is_full(self):
        if self.moves == 9:
            return True
        else:
            return False

    def is_game_over(self):
        if self.is_full() is True:
            return True
        elif self.calc_winner() is True:
            return True
        else:
            return False

p1 = player('Player 1', 'X')
p2 = player('Player 2', 'O')
TTT = game()
game_over = False
next_turn = p2

print(f'{p1.player} is {p1.letter}s.\n{p2.player} is {p2.letter}s')
for y in range(1,4):
    if all(x == ('x' or 'o') for x in board_in[y]['right']):
        print(x)
        print('yay')
    else:
        print(y)
        print('boo')
# while game_over == False:
#     print(board_in[1]['left']+'|'+board_in[1]['center']+'|'+board_in[1]['right'])
#     print(board_in[2]['left']+'|'+board_in[2]['center']+'|'+board_in[2]['right'])
#     print(board_in[3]['left']+'|'+board_in[3]['center']+'|'+board_in[3]['right'])
#     # turn check
#     turn = TTT.turn(p1,p2)
#     print(f"{turn.player}'s turn!")
#     # player of turn move
#     print(f'Where would you like to go?')

#     space = False
#     while space is False:
#         row = input('Top middle or bottom  ').lower()
#         column = input('Left center or right  ').lower()
#         if row in row_names and column in column_names:
#             space = TTT.move(row,column,turn.letter)
#         else:
#             print('Position unclear, try again')

#     # winner and game over check
#     # winner = TTT.calc_winner()
#     TTT.is_full()
#     game_over = TTT.is_game_over()

#     # if game not over, turn pass
#     next_turn = TTT.turn(p1,p2)