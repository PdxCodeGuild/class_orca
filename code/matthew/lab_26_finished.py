'''
Lab 26 Finished

'''


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        return self.name

class Game:
    def __init__(self):
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]

    def __repr__(self):
        board = self.board
        return f'{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}' \
               f'\n{board[6]}|{board[7]}|{board[8]}'

    def move(self, i, player):
        if i == "top left":
            i = 0
        elif i == "top middle":
            i = 1
        elif i == "top right":
            i = 2
        elif i == "middle left":
            i = 3
        elif i == "middle middle":
            i = 4
        elif i == "middle right":
            i = 5
        elif i == "bottom left":
            i = 6
        elif i == "bottom middle":
            i = 7
        elif i == "bottom right":
            i = 8
        else:
            return False

        self.board[i] = player.token

    def calc_winner(self):
        # check top row win condition
        if game_board.board[0] == 'x' and game_board.board[1] == 'x' and game_board.board[2] == 'x':
            return True
        elif game_board.board[0] == 'y' and game_board.board[1] == 'y' and game_board.board[2] == 'y':
            return True

        # check middle row win condition
        if game_board.board[3] == 'x' and game_board.board[4] == 'x' and game_board.board[5] == 'x':
            return True
        elif game_board.board[3] == 'y' and game_board.board[4] == 'y' and game_board.board[5] == 'y':
            return True
            # check bottom row win condition
        if game_board.board[6] == 'x' and game_board.board[7] == 'x' and game_board.board[8] == 'x':
            return True
        elif game_board.board[6] == 'y' and game_board.board[7] == 'y' and game_board.board[8] == 'y':
            return True

            # check left vertical win condition
        if game_board.board[0] == 'x' and game_board.board[3] == 'x' and game_board.board[6] == 'x':
            return True
        elif game_board.board[0] == 'y' and game_board.board[3] == 'y' and game_board.board[6] == 'y':
            return True

            # check middle vertical win condition
        if game_board.board[1] == 'x' and game_board.board[4] == 'x' and game_board.board[7] == 'x':
            return True
        elif game_board.board[1] == 'y' and game_board.board[4] == 'y' and game_board.board[7] == 'y':
            return True

            # check right vertical win condition
        if game_board.board[2] == 'x' and game_board.board[5] == 'x' and game_board.board[8] == 'x':
            return True
        elif game_board.board[2] == 'y' and game_board.board[5] == 'y' and game_board.board[8] == 'y':
            return True

            # check top left to bottom right win condition
        if game_board.board[0] == 'x' and game_board.board[4] == 'x' and game_board.board[8] == 'x':
            return True

        elif game_board.board[0] == 'y' and game_board.board[4] == 'y' and game_board.board[8] == 'y':
            return True

            # check bottom  left to top right win condition
        if game_board.board[6] == 'x' and game_board.board[4] == 'x' and game_board.board[2] == 'x':
            return True
        elif game_board.board[6] == 'y' and game_board.board[4] == 'y' and game_board.board[2] == 'y':
            return True


    def is_full(self):
        for i in self.board:
            if ' ' not in self.board:
                return True


    def is_game_over(self):
        if self.calc_winner() == True:
            print(f"Three in a row!")
            quit()
        elif self.is_full() == True:
            print("cats game")
            quit()

game_board = Game()

def name_assignment():
    print('Welcome to Tic-Tac_Toe')
    player1 = Player(input("Player one, please enter your name: "), 'x')
    print(f'Greetings {player1.name} you are the x token')
    print()
    player2 = Player(input("Player two, please enter your name: "), 'y')
    print(f'Greetings {player2.name} you are the y token')
    print()
    return player1, player2

player1, player2 = name_assignment()

def instructions():
    input(f'''
Press enter to continue and to receive the instructions: ''')
    print('''
In order to play, you will enter two commands.
The first command is: top, middle, or bottom
The second command is: left, right, or middle

Here is an example of top right:
 | |x
 | |
 | |
 
Press enter and the game will begin!
    ''')

instructions()

def main():
    counter = 0
    while True:
        i = input(f"enter your move ")
        if counter % 2 == 0:
            counter += 1
            print(f"{player2.name}'s turn: ")
            player_token = player1.token
            player = player1
        else:
            print(f"{player1.name}'s turn: ")
            counter += 1
            player_token = player2.token
            player = player2
        game_board.is_full()
        game_board.move(i, player)
        if game_board.move(i, player) == False:
            print("invalid move")
            print()
            i = input("enter your move ")
            game_board.move(i, player)
        game_board.calc_winner()
        print(game_board)
        game_board.is_game_over()

main()


