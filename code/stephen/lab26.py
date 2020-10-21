import random

inst_board = {'7': '7' , '8': '8' , '9': '9' ,
         '4': '4' , '5': '5' , '6': '6' ,
         '1': '1' , '2': '2' , '3': '3' }

board = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }

tokens = []
name = []
p1toke = []
p2toke = []

count = 0
turn = 'X'

class Player:
    def __init__(self):
        self.name = name
        # self.token = token

    def select_token(self, p1, p2):
        ht = input(f'{p1}, call (h)eads or (t)ails: \n>')
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            coin_flip = 'h'
        elif coin_flip == 1:
            coin_flip = 't'
        if ht == coin_flip:
            print(f'\n{p1} is X and goes first!')
            p1token = 'X'
            p2token = 'O'
            tokens.append(p1token)
            tokens.append(p2token)
            p1toke.append(p1token)
            p2toke.append(p2token)
        elif ht != coin_flip:
            print(f'{p2} is X and goes first!')
            p1token = 'O'
            p2token = 'X'
            tokens.append(p1token)
            tokens.append(p2token)
            p1toke.append(p1token)
            p2toke.append(p2token)
        return p1token, p2token

    def select_name(self):
        p1 = input('What is the name of Player 1?\n>')
        p2 = input('What is the name of Player 2?\n>')
        print('Player 1: ' + p1 + ', Player 2: ' + p2)
        name.append(p1)
        name.append(p2)
        return p1, p2


class Game:
    def __init__(self):
        self.board = board

    def print_board(self):
        print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
        print('--+---+--')
        print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
        print('--+---+--')
        print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

    def make_moves(self):
        turn = 'X'
        count = 0
        p1 = name[0]
        p2 = name[1]
        g.print_board()
        while True:    
            if p1toke[0] == turn:
                player = p1
                play = input(f'{player} is up!  Where would you like to move?\n>')
                if board[play] == ' ':
                    board[play] = turn
                    count += 1
                else:
                    print('That spot is already taken.  Try again.') 
                    continue
                if count >= 5:
                    g.calc_winner(player)

                if count == 9:
                    print('\nTie!\n')
                    replay()
                
                if player == p1:
                    player = p2
                else: 
                    player = p1
            
                g.print_board()
            
            elif p2toke[0] == turn:
                player = p2
                play = input(f'{player} is up!  Where would you like to move?\n>')
                if board[play] == ' ':            
                    board[play] = turn
                    count += 1
                else: 
                    print('That spot is already taken.  Try again.') 
                    continue
                if count >= 5:
                    g.calc_winner(player)

                if count == 9:
                    print('\nTie!\n')
                    replay()
                
                if player == p1:
                        player = p2
                else: 
                    player = p1
                g.print_board()
            
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'

            

    def calc_winner(self, player):
        
        if board['1'] == board['2'] == board['3'] != ' ':
            print(f'\n{player} is the Winner!\n')
            replay()
        elif board['1'] == board['4'] == board['7'] != ' ':
            print(f'\n{player} is the Winner!\n')
            replay()
        elif board['2'] == board['5'] == board['8'] != ' ':
            print(f'\n{player} is the Winner!\n')
            replay()
        elif board['3'] == board['6'] == board['9'] != ' ':
            print(f'\n{player} is the Winner!\n')
            replay()
        elif board['4'] == board['5'] == board['6'] != ' ':
            print(f'\n{player} is the Winner!\n')
            replay()
        elif board['7'] == board['8'] == board['9'] != ' ':
            print(f'\n{player} is the Winner!\n')
            replay()
        elif board['1'] == board['5'] == board['9'] != ' ':
            print(f'\n{player} is the Winner!\n')
            replay()
        elif board['7'] == board['5'] == board['3'] != ' ':
            print(f'\n{player} is the Winner!\n')
            replay()

def replay():
    g.print_board
    ask = input('Would you like to play again?  y/n:\n>')
    if ask == 'y':
        board.update((k, ' ') for k in board)
        g.print_board
        main()
    if ask == 'n':
        quit()
            
def instructions():
    print('''Two players will take turns placing their token, either X or O, in a 3x3 grid.  
First player to get three of their tokens in a row wins!  If the board is filled without a winner it is a tie.
You will input the number of the grid you would like to place your token.  The grids are labelled as such:''')
    print(inst_board['7'] + ' | ' + inst_board['8'] + ' | ' + inst_board['9'])
    print('--+---+--')
    print(inst_board['4'] + ' | ' + inst_board['5'] + ' | ' + inst_board['6'])
    print('--+---+--')
    print(inst_board['1'] + ' | ' + inst_board['2'] + ' | ' + inst_board['3'])
    mm = input('Press enter to go to the menu')
    main()

def main():
    
    p.select_name()
    p1 = name[0]
    p2 = name[1]
    p.select_token(p1, p2)
    nt_list = dict(zip(name, tokens))
    print(nt_list)
    g.make_moves()

p = Player()
g = Game()

ask_inst = input('Welcome to Tic-Tac-Toe!  Would you like to read the instructions?  y/n:\n>')
if ask_inst == 'y':
    instructions()

main()