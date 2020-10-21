# Lab26 Tic-Tac-Toe

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
    def __str__(self):
        return self.name


class Game:
    def __init__(self):
        self.board = [" "] * 9
    
    def display (self):
        print(self.board[0] +"|" + self.board[1] + "|" + self.board[2])
        print(self.board[3] +"|" + self.board[4] + "|" + self.board[5])
        print(self.board[6] +"|" + self.board[7] + "|" + self.board[8])
    
    def move(self, x, player):

        #take in coordinates and put them on the board
        if self.board[x-1] == " ":
            self.board[x-1] = player.token
            return player
        else:
            print("That square's already taken!")

    def calc_winner(self):
        pass

    def is_full(self):
        pass

    def game_over(self):
        pass


new_game = Game()

def main(new_game):
    print(new_game.display())

    player1 = Player(input("What's your name? "), "X")

    print(player1)

    player2 = Player(input("What's your name? "), "O")
    print(player2)

    while True:
        new_game.move(int(input("What's the square, Player 1?  " )), player1)
        new_game.display()

        new_game.move(int(input("What's the square, Player 2?  " )), player2)
        new_game.display()

main(new_game)

