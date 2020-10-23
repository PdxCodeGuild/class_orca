import math
board_in = {
     1: {'left': ' ', 'center': ' ', 'right': ' '},
     2: {'left': ' ', 'center': ' ', 'right': ' '},
     3: {'left': ' ', 'center': ' ', 'right': ' '}
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

    def move(self, row, column, turn):
        self.moves += 1
        rows = {'top': 1, 'middle': 2, 'bottom':3}
        self.row = rows[row]
        self.column = column
        board_in[self.row][self.column] = turn
 
    def is_full(self):
        if self.moves == 9:
            return True
        else:
            return False

    def is_game_over(self):
        if self.is_full() == True:
            return True
        else:
            return False

    # def __repr__(self):
    #     return f'{self.
p1 = player('Player 1', 'X')
p2 = player('Player 2', 'O')
TTT = game()
game_over = False
next_turn = p2

while game_over == False:
    print(f'{p1.player} is {p1.letter}s.\n{p2.player} is {p2.letter}s')

    print(board_in[1]['left']+'|'+board_in[1]['center']+'|'+board_in[1]['right'])
    print(board_in[2]['left']+'|'+board_in[2]['center']+'|'+board_in[2]['right'])
    print(board_in[3]['left']+'|'+board_in[3]['center']+'|'+board_in[3]['right'])
    
    turn = TTT.turn(p1,p2)
    print(f"{turn.player}'s turn!")
    print(f'where would you like to go?')
    row = input('Top middle or bottom  ').lower()
    column = input('Left center or right  ').lower()

    TTT.move(row,column,turn.letter)
    next_turn = TTT.turn(p1,p2)

    TTT.is_full()
    game_over = TTT.is_game_over()
