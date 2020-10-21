class Player:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name


class Game:
    def __init__(self):
        self.cells = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def board(self):
        print('\n %s | %s | %s ' %(self.cells[1], self.cells[2], self.cells[3]))
        print('-----------')
        print(' %s | %s | %s ' %(self.cells[4], self.cells[5], self.cells[6]))
        print('-----------')
        print(' %s | %s | %s ' %(self.cells[7], self.cells[8], self.cells[9]))

    def move(self, cell, player):
        self.cells[cell] = player

    def calc_winner(self):
        # 1,2,3 or 4,5,6 or 7,8,9 or 1,4,7 or 2,5,8 or 3,6,9 or 1,5,9 or 3,5,7
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
    def is_full(self):
        pass
    def is_game_over(self):
        pass

game = Game()

player1 = Player(input('Player 1 enter name: '))
player2 = Player(input('Player 2 enter name: '))

def main():
    print('Tic Tac Toe\n')
    while True:
        game.board()
        player1_choice = int(input(f'\n{player1} choose 1 - 9 \n> '))
        game.move(player1_choice, 'X')
        if game.calc_winner():
            game.board()
            print(f'{player1} wins')
            break
        else:
            game.board()
            player2_choice = int(input(f'\n{player2} choose 1 - 9 \n> '))
            game.move(player2_choice, 'O')
            if game.calc_winner():
                game.board()
                print(f'{player2} wins')
                break
            else:
                pass




main()
