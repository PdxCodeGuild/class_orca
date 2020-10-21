##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# ***************************** WORKING FROM HERE *****************************
# ***************************** ^^^^^^^^^ TO HERE *****************************
                        
board_indices = [       '0', '1', '2',
                        '3', '4', '5',
                        '6', '7', '8'   ] # INDICES ONLY
##############################################################################

class Player():
    def __init__(self,token,name='player1'):
        self.token = token
        self.name = name

class Board():
    def __init__(self, winner=''):
        self.winner = winner                                                                 ##### TODO CHANGE BOARD IN FINAL #####
        self.board = [  ' ', ' ', ' ',
                        ' ', ' ', ' ',
                        ' ', ' ', ' '   ]

    def __repr__(self):
        return f'{self.board[0]} | {self.board[1]} | {self.board[2]}\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n{self.board[6]} | {self.board[7]} | {self.board[8]}'

    def move(self, position, player):
        # TODO FIX INPUT EXCESSIVE RANGE... TEST ONLY 1-9, PERHAPS USING TODAY'S LESSON ON REGULAR EXPRESSIONS
        # TODO FIX INPUT EXCESSIVE RANGE... TEST ONLY 1-9, PERHAPS USING TODAY'S LESSON ON REGULAR EXPRESSIONS
        # TODO FIX INPUT EXCESSIVE RANGE... TEST ONLY 1-9, PERHAPS USING TODAY'S LESSON ON REGULAR EXPRESSIONS
        if self.board[position-1] != ' ':
            print(f'Invalid entry. Position: {position} is currently full! Please try again or type \"help\".')
            return False
        else:
            self.board[position-1] = f'{player.token}'             # PLACE THE TOKEN!
            print(f'Player \"{player.name}\" places \"{player.token}\" at position {position}:')
            print(self.__repr__())
            return True

    def calc_winner(self):
            # POSSIBLE WINNING INDICES in if statement below:
            # 012 # horizontal win1             # 345 # horizontal win2             # 678 # horizontal win3
            # 036 # vertical win1               # 147 # vertical win2               # 258 # vertical win3
            # 048 # diagonal win1/2             # 246 # diagonal win2/2
        if ( self.board[0] == self.board[1] == self.board[2] ) or ( self.board[3] == self.board[4] == self.board[5] ) or ( self.board[6] == self.board[7] == self.board[8] ) or ( 
            self.board[0] == self.board[3] == self.board[6] ) or ( self.board[1] == self.board[4] == self.board[7] ) or ( self.board[2] == self.board[5] == self.board[8] ) or ( 
            self.board[0] == self.board[4] == self.board[8] ) or ( self.board[2] == self.board[4] == self.board[6] ) :
            print('winner!winner!winner!winner!winner!winner!winner!winner!')
            self.winner = self.board[0] ###################################################     ##### TODO CHANGE IN FINAL #####
            return True                  # TODO return winner?
        else:
            return False

    def is_full(self):
        filled_positions = 0
        for i in range(9):
            if self.board[i] == 'X' or self.board[i] == 'O':
                filled_positions += 1
        if filled_positions == 9:
            return True
        else:
            return False

    def is_game_over(self):
        if self.calc_winner() == True:
            print(f'Congratulations -- {True} won the game!') ############     ##### CHANGE IN FINAL ##### # REMOVE these print statemnts, because this function has no player, and put them in the REPL
            return True
        else:               
            if self.is_full() == True:
                print('Board is full. Game over.') ##### CHANGE IN FINAL #####
                print('Boring outcome -- both players lost!') ##### CHANGE IN FINAL #####
                return True
            else:
                return False

helper_board = Board()
helper_board.board = [      '1', '2', '3',
                            '4', '5', '6',
                            '7', '8', '9'   ] # OK TO PRINT FOR HELPING USER 

##############################################################################

john = Player('X', 'John')
computer = Player('O','computer')
board1 = Board()

# # TEST MOVES
# board1.move(5,computer)
# board1.move(3,john)
# board1.move(2,computer)
# board1.move(1,john)
# board1.move(2,computer)
# board1.move(8,computer)
# board1.is_game_over()

# Step 4 main() input REPL
def next_operation():
    user_input = input(f'Enter next operation: ')
    return user_input

def main():
    print('Welcome to TIC-TAC-TOE v1.0!')
    user_input = ''

    user_input = ''                                  ##### REMOVE IN FINAL, TESTING ONLY #####

    if user_input == 'help':
        print('Think of the board positions like an old phone keypad, numbered from top left to bottom right:')
        print(helper_board.__repr__())
        # user_input = next_operation()


main()
# print(board1.__repr__())









# TEST BOARDS
    # test_board_blank = [    ' ', ' ', ' ',
    #                         ' ', ' ', ' ',
    #                         ' ', ' ', ' '   ]

    # test_board_1 = [        'X', 'O', 'O',
    #                         'X', 'O', 'X',
    #                         'O', 'X', 'O'   ] # FULL, NO WINNER

    # test_board_2 = [        'X', 'O', 'X',
    #                         'X', 'O', 'O',
    #                         'O', 'X', 'X'   ] # FULL, NO WINNER

    # test_board_3 = [        'X', 'X', 'X',
    #                         'O', 'O', 'X',
    #                         'X', 'O', 'O'   ] # X WINS

    # test_board_4 = [        'X', 'O', 'O',
    #                         'O', 'O', 'X',
    #                         'X', 'O', 'X'   ] # O WINS

    # test_board_5 = [        'X', 'O', 'O',
    #                         'O', ' ', 'X',
    #                         'X', 'O', 'X'   ] # NOT FULL


print('    >> PROGRAM ENDED <<    ')
##############################################################################
    
                                        # IN CASE I WANT LISTS OF LISTS:
                                        # self.board = [  [' '],[' '],[' '],
                                        #                 [' '],[' '],[' '],
                                        #                 [' '],[' '],[' ']   ]
    # coord = [(x,y) for x in range(4) for y in range(4)]
    # HINTS
    # easiest way...
    # build classes using EXACT properties (self) and methods he's given us...
    # two classes, game class has those methods...
    # then go ahead and build a REPL to let the user play...
    # REMEMBER THE ATM LAB AND REPEAT THE PROCESS...
    # Q: HOW TO BEST REPRESENT THE BOARD?
    # board list, tuples, or dict
    # list of lists [] x and y value
    # TUPLES... sometimes do dictionaries, some do dict 

    ##############################################################################
    # copy of steps:

    # Step 1 WRITE TWO CLASSES. First, Class Player():
    # 1a two properties: name and token X or O. both in self in init function
    # Step 2 Second, Class Game():
    # 2a property self.board = board, start with list of board here # OPTIONS FUTURE are tuple or dictionary
    # Step 3 Methods in Class Game:
    # 3a __repr__ function, which prints the board
    # 3b move(x,y,player) function "Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position."
    # 3b take the player's coordinates and input their character string -- NO INPUT YET, that's for the REPL loop... 
    # 3c calc_winner() function which RUNS EACH TURN to RETURN NONE or which string (X or O) has won
    # 3d is_full() which returns TRUE if board is full, ENDS GAME
    # 3e is_game_over() function which returns TRUE if board is full or player has won, i think this runs each time...
    # Step 4 main() input REPL
    # Step 10 # NEXT FUTURE make computer player_2, use random to pick a random spot to place its 'O'
    ##############################################################################

    ##############################################################################
    # https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab26-tictactoe.md copy
    ##############################################################################

    # Lab 26: Tic-Tac-Toe

    # Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

    # You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

    # The Player class has the following properties:

    #     name = player name
    #     token = 'X' or 'O'

    # The Game class has the following properties:

    #     board = your representation of the board

    # You can represent the board however you like, such as a 2D list, tuples, or dictionary.

    # The Game class has the following methods:

    #     __repr__() Returns a pretty string representation of the game board

    # >>> print(board)
    # X| | 
    # O|X|O
    #  | | 

    #     move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.

    # >>> board.move(2, 1, player_1)
    #  | | 
    #  | |X
    #  | | 

    #     calc_winner() What token character string has won or None if no one has.

    # X| | 
    # O|X|O
    #  | |X
    # >>> board.calc_winner()
    # X

    #     is_full() Returns true if the game board is full.

    # X|O|X
    # X|X|O
    # O|O|X
    # >>> board.is_full()
    # True

    #     is_game_over() Returns true if the game board is full or a player has won.

    # X|O|X
    # X|X|O
    # O|O|X
    # >>> board.is_game_over()
    # True

    # X|O|
    #  | |X
    #  | |
    # >>> board.is_game_over()
    # False