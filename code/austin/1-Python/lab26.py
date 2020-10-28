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
        print(f"☆ Tic-Tac-Toe ☆")
        print("  " + self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("  " + self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("  " + self.board[6] + " | " + self.board[7] + " | " + self.board[8])
    
    def move(self, x, player):
        if self.board[x-1] == " ":
            self.board[x-1] = player.token
            return player
        else:
            print("That square's already taken!")

    def calc_winner(self, player):
        for i in range(0, 9):
            if self.board[0] == self.board[1] == self.board[2] != " ":
                print(f'You won, {player}!')
                break
            elif self.board[3] == self.board[4] == self.board[5] != " ":
                print(f'You won, {player}!')
                break
            elif self.board[6] == self.board[7] == self.board[8] != " ":
                print(f'You won, {player}!')
                break
            elif self.board[0] == self.board[3] == self.board[6] != " ":
                print(f'You won, {player}!')
                break
            elif self.board[1] == self.board[4] == self.board[7] != " ":
                print(f'You won, {player}!')
                break
            elif self.board[2] == self.board[5] == self.board[8] != " ":
                print(f'You won, {player}!')
                break
            elif self.board[0] == self.board[4] == self.board[8] != " ":
                print(f'You won, {player}!')
                break
            elif self.board[2] == self.board[4] == self.board[6] != " ":
                print(f'You won, {player}!')
                break
            else: 
                return False

    def is_full(self):
        for i in range(9):
            if self.board[i] == " ":
                return False
            
    def game_over(self, player):
        if new_game.calc_winner(player) != False:
            print("Game over! ¯\_(ツ)_/¯ ")
            again = input("Play again? y/n  ")
            if again == "y":
                self.board = [" "] * 9
            else:
                quit()
        elif new_game.is_full() != False:
            print("Cat's game!")
            again = input("Play again? y/n  ")
            if again == "y":
                self.board = [" "] * 9
            else:
                quit()

new_game = Game()

def main(new_game):
    print(new_game.display())

    player1 = Player(input("What's your name, Player 1? "), "X")

    print(player1)

    player2 = Player(input("What's your name, Player 2? "), "O")
    print(player2)

    while True:
        new_game.move(int(input("What's the square, Player 1?  " )), player1)
        new_game.display()

        new_game.game_over(player1)

        new_game.move(int(input("What's the square, Player 2?  " )), player2)
        new_game.display()

        new_game.game_over(player2)
        
main(new_game)