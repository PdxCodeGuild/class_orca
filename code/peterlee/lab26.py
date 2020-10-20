class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token 


class Game:
    #initializes the game board and fills it to ensure __repr__ does not go out of index
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append([' ',' ',' '])
    
    #prints out the board according to the self.board list joined by |
    def __repr__(self):
        for x in range(3):
            print('|'.join(self.board[x]))
        return

    #inserts the player's move into self.board list based on their inputs
    def move(self, x, y, player_token, other_player_token):
        if self.board[x][y] == other_player_token:
            return False
        del self.board[x][y]
        self.board[x].insert(y, player_token)
        return

    #brute forced if statements to check for winner
    def calc_winner(self, player1token, player2token):
        if self.board[0][0] == player1token and self.board[1][1] == player1token and self.board[2][2] == player1token:
            return player1token
        elif self.board[0][0] == player2token and self.board[1][1] == player2token and self.board[2][2] == player2token:
            return player2token
        elif self.board[0][2] == player1token and self.board[1][1] == player1token and self.board[2][0] == player1token:
            return player1token
        elif self.board[0][2] == player2token and self.board[1][1] == player2token and self.board[2][0] == player2token:
            return player2token
        elif self.board[0][0] == player1token and self.board[0][1] == player1token and self.board[0][2] == player1token:
            return player1token
        elif self.board[0][0] == player2token and self.board[0][1] == player2token and self.board[0][2] == player2token:
            return player2token
        elif self.board[1][0] == player1token and self.board[1][1] == player1token and self.board[1][2] == player1token:
            return player1token
        elif self.board[1][0] == player2token and self.board[1][1] == player2token and self.board[1][2] == player2token:
            return player2token
        elif self.board[2][0] == player1token and self.board[2][1] == player1token and self.board[2][2] == player1token:
            return player1token
        elif self.board[2][0] == player2token and self.board[2][1] == player2token and self.board[2][2] == player2token:
            return player2token
        elif self.board[0][0] == player1token and self.board[1][0] == player1token and self.board[2][0] == player1token:
            return player1token
        elif self.board[0][0] == player2token and self.board[1][0] == player2token and self.board[2][0] == player2token:
            return player2token
        elif self.board[0][1] == player1token and self.board[1][1] == player1token and self.board[2][1] == player1token:
            return player1token
        elif self.board[0][1] == player2token and self.board[1][1] == player2token and self.board[2][1] == player2token:
            return player2token
        elif self.board[0][2] == player1token and self.board[1][2] == player1token and self.board[2][2] == player1token:
            return player1token
        elif self.board[0][2] == player2token and self.board[1][2] == player2token and self.board[2][2] == player2token:
            return player2token
        else:
            return None

    #checks if the game board is full by checking if all 9 spots are filled with X's or O's
    def is_full(self):
        is_full_list = []
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 'X' or self.board[x][y] == 'O':
                    is_full_list.append('F')
        if len(is_full_list) == 9:
            return True
        else:
            return False
    #checks if the game is over by looking at is_game_over method and calc_winner method
    def is_game_over(self, P1token, P2token):
        if self.is_full() == True or self.calc_winner(P1token, P2token) == P1token or self.calc_winner(P1token, P2token) == P2token:
            return True
        else:
            return False 



def main():
    tokens = ['X', 'O']
    player_one_name = input("What is the first player's name? ")
    player_one_token = input("Would they like to be an X or an O? ")
    #removes pl's token from the pool
    tokens.remove(player_one_token)
    remaining_tokens = tokens.pop()

    P1 = Player(player_one_name, player_one_token)

    player_two_name = input("What is the second player's name? ")
    player_two_token = input("Would they like to be an X or an O? ")
    #forces p2 to take the remaining option if they choose p1's token
    if player_one_token == player_two_token:
        print(f"I'm sorry, but Player 1 already took that token so they are stuck with {remaining_tokens}")
        player_two_token = remaining_tokens
    
    P2 = Player(player_two_name, player_two_token)

    new_game = Game()
    repr(new_game.__repr__())
    #REPL that runs each player's turn in order
    while True:
        player_one_turn_x = int(input(f'{P1.name}, which row would you like to place an {P1.token} from 0-2? (0 is the top row) '))
        player_one_turn_y = int(input(f'Which column would you like to place the {P1.token} from 0-2? (0 is the left column)'))
        new_game.move(player_one_turn_x, player_one_turn_y, P1.token, P2.token)
        #makes sure that the player does not overwrite their opponent's move
        while new_game.move(player_one_turn_x, player_one_turn_y, P1.token, P2.token) == False:
            print(f'Sorry but you cannot place an {P1.token} there. Please select your row and column again. ')
            player_one_turn_x = int(input(f'{P1.name}, which row would you like to place an {P1.token} from 0-2? (0 is the top row) '))
            player_one_turn_y = int(input(f'Which column would you like to place the {P1.token} from 0-2? (0 is the left column)'))
        repr(new_game.__repr__())
        #loop that checks whether the game is over after every move
        if new_game.is_game_over(P1.token, P2.token) == True:
            if new_game.is_full() == True:
                print('The board is full. The game is a draw.')
                break
            elif new_game.is_full() == False:
                if new_game.calc_winner(P1.token, P2.token) == P1.token:
                    print(f'{P1.name} wins!')
                    break
                elif new_game.calc_winner(P1.token, P2.token) == P2.token:
                    print(f'{P2.name} wins!')
                    break

        player_two_turn_x = int(input(f'{P2.name}, which row would you like to place an {P2.token} from 0-2? (0 is the top row) '))
        player_two_turn_y = int(input(f'Which column would you like to place the {P2.token} from 0-2? (0 is the left column)'))
        new_game.move(player_two_turn_x, player_one_turn_y, P2.token, P1.token)
        while new_game.move(player_two_turn_x, player_two_turn_y, P2.token, P1.token) == False:
            print(f'Sorry but you cannot place an {P2.token} there. Please select your row and column again. ')
            player_two_turn_x = int(input(f'{P2.name}, which row would you like to place an {P2.token} from 0-2? (0 is the top row) '))
            player_two_turn_y = int(input(f'Which column would you like to place the {P2.token} from 0-2? (0 is the left column)'))
        repr(new_game.__repr__())

        if new_game.is_game_over(P1.token, P2.token) == True:
            if new_game.is_full() == True:
                print('The board is full. The game is a draw.')
                break
            elif new_game.is_full() == False:
                if new_game.calc_winner(P1.token, P2.token) == P1.token:
                    print(f'{P1.name} wins!')
                    break
                elif new_game.calc_winner(P1.token, P2.token) == P2.token:
                    print(f'{P2.name} wins!')
                    break

main()
