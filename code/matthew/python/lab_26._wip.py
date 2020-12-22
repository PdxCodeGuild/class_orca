#
# board = [
#
#     line1 = [' ','|','|',' ']
#     line2 = [' ','|','|',' ']
#     line3 = [' ','|','|',' ']
# ]




class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        return self.name

class Game:
    def __init__(self):
        self.board = ['','','','','','','','','','']


    def __repr__(self):
        board = self.board
        return f'{board[0]}|{board[1]}|{board[3]}\n{board[4]}|{board[5]}|{board[6]}\n{board[7]}|{board[8]}|{board[9]}'



    def move(self, x, y, player):
        return self.move,

    def calc_winner(self):
        return self.calc_winner()

    def is_full(self):
        return self.is_full()

    def is_game_over(self):
        return self.is_game_over()


game_board = Game()


def name_assignment():
    print('Welcome to Tic-Tac_Toe')
    player1 = Player(input("Player one, please enter your name: "),'x')
    print(f'Greetings {player1.name} you are the x token')
    print()
    player2 = Player(input("Player two, please enter your name: "), 'y')
    print(f'Greetings {player2.name} you are the y token')


name_assignment()

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





def gameplay():
    print("Current Board")
    print(*line1)
    print(*line2)
    print(*line3)
    print()
    print(f"NAME, it is your turn")
    turn = input("Please enter your move (example 'top middle'): ")

    if turn == "top left":
        line1[0] = 'x'
        game_board = Game()
        # print(*line1)
    else:
        instructions()



gameplay()

# print(*line1)
# print(*line2)
# print(*line3)





