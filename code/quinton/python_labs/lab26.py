# Lab26 by Quinton Baseman
class Player:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
class Game:
    def __init__(self):
        self.cells = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    #setting up the board using string formatting with rows 
    def board(self):
        print('\n %s | %s | %s ' %(self.cells[1], self.cells[2], self.cells[3]))
        print('-----------')
        print(' %s | %s | %s ' %(self.cells[4], self.cells[5], self.cells[6]))
        print('-----------')
        print(' %s | %s | %s ' %(self.cells[7], self.cells[8], self.cells[9]))
    #if the cell is empty the player can move there, if not it'll prompt to choose an empty cell
    def move(self, cell, player):
        if self.cells[cell] == ' ':
            self.cells[cell] = player
        else:
            re_try = int(input('Invalid. choose 1 - 9 \n> '))
            self.move(re_try, player)
    #checking for all winning combos and returning true if a player won
    def calc_winner(self):
        if self.cells[1] == 'X' and self.cells[2] == 'X' and self.cells[3] == 'X' or \
            self.cells[4] == 'X' and self.cells[5] == 'X' and self.cells[6] == 'X' or \
            self.cells[7] == 'X' and self.cells[8] == 'X' and self.cells[9] == 'X' or \
            self.cells[1] == 'X' and self.cells[4] == 'X' and self.cells[7] == 'X' or \
            self.cells[2] == 'X' and self.cells[5] == 'X' and self.cells[8] == 'X' or \
            self.cells[3] == 'X' and self.cells[6] == 'X' and self.cells[9] == 'X' or \
            self.cells[1] == 'X' and self.cells[5] == 'X' and self.cells[9] == 'X' or \
            self.cells[3] == 'X' and self.cells[5] == 'X' and self.cells[7] == 'X' or \
            self.cells[1] == 'O' and self.cells[2] == 'O' and self.cells[3] == 'O' or \
            self.cells[4] == 'O' and self.cells[5] == 'O' and self.cells[6] == 'O' or \
            self.cells[7] == 'O' and self.cells[8] == 'O' and self.cells[9] == 'O' or \
            self.cells[1] == 'O' and self.cells[4] == 'O' and self.cells[7] == 'O' or \
            self.cells[2] == 'O' and self.cells[5] == 'O' and self.cells[8] == 'O' or \
            self.cells[3] == 'O' and self.cells[6] == 'O' and self.cells[9] == 'O' or \
            self.cells[1] == 'O' and self.cells[5] == 'O' and self.cells[9] == 'O' or \
            self.cells[3] == 'O' and self.cells[5] == 'O' and self.cells[7] == 'O':
            return True
    #returning true if the board is full and nobody won
    def is_full(self):
        if self.cells[1] in ['X','O'] and self.cells[2] in ['X','O'] and self.cells[3] in \
            ['X','O'] and self.cells[4] in ['X','O'] and self.cells[5] in ['X','O'] and self.cells[6] in \
                ['X','O'] and self.cells[7] in ['X','O'] and self.cells[8] in ['X','O'] and self.cells[9] in ['X','O'] \
                    and not game.calc_winner():
            return True
    #returning true if there is a winner or the board is full
    def is_game_over(self):
        if game.calc_winner() or game.is_full():
            return True

game = Game()

player1 = Player(input('Player 1 enter name: '))
player2 = Player(input('Player 2 enter name: '))

def main():
    print('Tic Tac Toe\n')
    while True:
        game.board()
        player1_choice = int(input(f'\n{player1} choose 1 - 9 \n> '))
        game.move(player1_choice, 'X')
        if game.is_full():
            game.board()
            print('\nTie Game!')
            break
        elif game.calc_winner():
            game.board()
            print(f'\n{player1} wins')
            break
        else:
            game.board()
            player2_choice = int(input(f'\n{player2} choose 1 - 9 \n> '))
            game.move(player2_choice, 'O')
            if game.is_full():
                game.board()
                print('\nTie Game!')
                break
            elif game.calc_winner():
                game.board()
                print(f'\n{player2} wins')
                break
            else:
                pass
main()