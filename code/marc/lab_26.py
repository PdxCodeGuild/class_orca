#This is lab 26 TIC TAC TOE

class Player:
    def __init__ (self, name, token = 0):
        self.name = name
        self.token = token
        # self.player = (self.name, self.token)
        # return self.player
        

    # def token_choice (self, token = "O"):
    #     self.token = token
    #     return self.token
    
    def player_maker (self):
        self.player = (self.name, self.token)
        return self.player


class Game:
    def __init__ (self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        
        self.board = [[" "," "," "], [" "," "," "], [" "," "," "]]
        
        self.board_move = {1:self.board[0][0], 2:self.board[0][1], 3:self.board[0][2],
        4:self.board[1][0], 5:self.board[1][1], 6:self.board[1][2],
        7:self.board[2][0], 8:self.board[2][1], 9:self.board[2][2] }
        
        # print(self.board_move)

    def __repr__(self):
        return f'''\n| {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |\n
| {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |\n
| {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |'''

    def choices(self):
        return "\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |"
    
    # def check_move(self, move_choice):
    #     self.move_choice = move_choice
    #     if self.move_choice < 1 or self.move_choice > 9:
    #         return False
    #     elif self.board_move[self.move_choice] == "X" or self.board_move[self.move_choice] == "O":
    #         print("That square is taken!")
    #         return False
    #     else:
    #         return True

    
    def move(self, player):
        if player == self.player_1:
            move = self.player_1[1]
        elif player == self.player_2:
            move = self.player_2[1]
        # make_move = True
        self.move_choice = (int(input(f'''Here is the game board \n{self.__repr__()}\n 
Choose a number between 1 and 9 to make your move {self.choices()}:
        \n''')))
#         if self.move_choice < 1 or self.move_choice > 9:
#             make_move = False
#         if self.board_move[self.move_choice] == "X" or self.board_move[self.move_choice] == "O":
#             make_move = False
#         while make_move == False:
#             self.move_choice = (int(input(f'''Here is the game board \n{self.__repr__()}\n 
# Choose a number between 1 and 9 to make your move {self.choices()}:
#         \n''')))
            


#         self.check_move(move_choice)
#         while self.check_move(move_choice) == False:
#             self.move_choice = (int(input(f'''Here is the game board \n{self.__repr__()}\n 
# Choose a number between 1 and 9 to make your move {self.choices()}:
#         \n''')))
            
        while self.move_choice < 1 or self.move_choice > 9:
            self.move_choice = (int(input(f'''Choose a number between 1 and 9 to make your move:\n''')))
        while self.board_move[self.move_choice] == "X" or self.board_move[self.move_choice] == "O":
           self.move_choice = (int(input(f'''That square is taken. Choose a number between 1 and 9 to make your move:\n''')))
        print(self.board_move[self.move_choice])
        if self.move_choice == 9:
            self.board[2][2] = move
        elif self.move_choice == 8:
            self.board[2][1] = move
        elif self.move_choice == 7:
            self.board[2][0] = move
        elif self.move_choice == 6:
            self.board[1][2] = move
        elif self.move_choice == 5:
            self.board[1][1] = move
        elif self.move_choice == 4:
            self.board[1][0] = move
        elif self.move_choice == 3:
            self.board[0][2] = move
        elif self.move_choice == 2:
            self.board[0][1] = move
        elif self.move_choice == 1:
            self.board[0][0] = move
        
        return f"Move made, here is the board{self.__repr__()}." 

    def calc_winner(self):
        if self.board[0] == ["O", "O", "O"] or self.board[0] == ["X", "X", "x"]:
            return True
        elif self.board[1] == ["O", "O", "O"] or self.board[1] == ["X", "X", "x"]:
            return True
        elif self.board[2] == ["O", "O", "O"] or self.board[2] == ["X", "X", "x"]:
           return True
        elif self.board [0][0] == "O" and self.board [1][0] == "O" and self.board [2][0] == "O" or\
        self.board [0][0] == "X" and self.board [1][0] == "X" and self.board [2][0] == "X":
            return True
        elif self.board [0][1] == "O" and self.board [1][1] == "O" and self.board [2][1] == "O" or\
        self.board [0][1] == "X" and self.board [2][1] == "X" and self.board [2][1] == "X":
            return True
        elif self.board [0][2] == "O" and self.board [1][2] == "O" and self.board [2][2] == "O" or\
        self.board [0][2] == "X" and self.board [1][2] == "X" and self.board [2][2] == "X":
            return True
        elif self.board [0][0] == "O" and self.board [1][1] == "O" and self.board [2][2] == "O" or\
        self.board [0][0] == "X" and self.board [1][1] == "X" and self.board [2][2] == "X":
            return True
        elif self.board [0][2] == "O" and self.board [1][1] == "O" and self.board [2][0] == "O" or\
        self.board [0][2] == "X" and self.board [1][1] == "X" and self.board [2][0] == "X":
            return True
        else:
            return False
        

    def is_full(self):
        self.yes = False
        for list in self.board:
            for character in list:
                if character == " ":
                    self.yes = False
                    break
                else:
                    self.yes = True
        return self.yes
        
    
    def is_game_over(self):
        if self.calc_winner() == True or self.is_full() == True:
            return True
        else:
            return False

def main(): 
    player_1_name = input ("Player 1 what is your name?\n")
    player_1_token = (input("X's or O's:\n")).capitalize()
    while player_1_token != "X" and player_1_token != "O":
        player_1_token = (input("X's or O's:\n")).capitalize()
    player_1 = Player(player_1_name, player_1_token)
    player_1 = player_1.player_maker()


    player_2_name = input ("Player 2 what is your name?:\n")
    if player_1_token == "O":
        player_2_token = "X"
    elif player_1_token == "X":
        player_2_token = "O"
    print(f"{player_2_name} you are {player_2_token}'s")
    player_2 = Player(player_2_name, player_2_token)
    player_2 = player_2.player_maker()
   
    game = Game(player_1, player_2)
    
    whose_turn = 1
    while game.is_game_over() == False:
        
        if whose_turn % 2 == 0:
            print(f"{player_2_name} it's your turn!")
            game.move(player_2)
            if game.calc_winner() == True:
                print(f"Congrats {player_2_name} you win!")
        else:
            print(f"{player_1_name} it's your turn!")
            game.move(player_1)
            if game.calc_winner() == True:
                print(f"Congrats {player_1_name} you win!")
        whose_turn +=1
        if game.is_full() == True:
            print("Board is full!")
            play_again = (input("Play again? y or n?:\n")).lower()
            while play_again != "y" and play_again != "n":
                (input("Play again? y or n?:\n")).lower()
            if play_again == "y":
                game.board = [[" "," "," "], [" "," "," "], [" "," "," "]]
            elif play_again != "y":
                print ("Good Game!")
                break
        if game.is_game_over() == True:
            play_again = (input("Play again? y or n?:\n")).lower()
            while play_again != "y" and play_again != "n":
                (input("Play again? y or n?:\n")).lower()
            if play_again == "y":
                game.board = [[" "," "," "], [" "," "," "], [" "," "," "]]
            elif play_again != "y":
                print ("Good Game!")
                break

main ()
       