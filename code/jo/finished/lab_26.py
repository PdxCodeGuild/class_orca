
# list of lists that will be the game board
game_board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

# defines a player with name and token
class Player:
    def __init__(self,name,token):
        self.name = name 
        self.token = token

# this class is the basic game
class Game:
    # import global variables for use
    global p1
    global p2
    # initializes the class
    def init (self,board):
        self.board = game_board

    # method that fills in a space on the game board with a player's token using input integers
    def move(x,y,player):
        if player == p1.name: 
            game_board[int(y-1)][int(x)-1] = p1.token
            return game_board
        else:
            game_board[int(y-1)][int(x)-1] = p2.token
            return game_board

    # prints out the game board lists as a string to represent a real game board
    def __repr__ (self):
        disp_board = f"""{game_board[0][0]}|{game_board[0][1]}|{game_board[0][2]}
{game_board[1][0]}|{game_board[1][1]}|{game_board[1][2]}
{game_board[2][0]}|{game_board[2][1]}|{game_board[2][2]}"""
        return disp_board

    # checks for different win conditions
    def calc_winner():
        # checks each item in each game board row. counts items that match first item, returns win if count gets to 3
        for row in game_board:
            count = 0
            match = row[count]
            for i in row:
                if i == match and i != " ":
                    count += 1
                if count == 3:
                    return "win"      

        # compares each item in the first game board list to each item at the same index in all lists. counts matches and returns win if 3
        for i in range(3):
            match = i
            counter = 0
            for row in game_board:
                if row[i] == game_board[0][i] and row[i] != " ":
                    counter += 1
                if counter == 3:
                    return "win"

        # checks for diagonal win conditions by evaluating each index needed for a win
        if game_board[0][2] == 'x' and game_board[1][1] == 'x' and game_board[2][0] == 'x':
            return "win"
        if game_board[0][0] == 'x' and game_board[1][1] == 'x' and game_board[2][2] == 'x':
            return "win"
        if game_board[0][2] == 'o' and game_board[1][1] == 'o' and game_board[2][0] == 'o':
            return "win"
        if game_board[0][0] == 'o' and game_board[1][1] == 'o' and game_board[2][2] == 'o':
            return "win"                                                           

    # checks if board is false. default is true, but if there is a space, will overwrite with false. if there's no empty spaces to return false, full will remain true
    def is_full():
        full = True
        for row in game_board:
            for i in row:
                if i == " ":
                    full = False
        if full:
            return "game_over"     

        
def main():

    global p1
    global p2
    # saves player names and the token they will be to a variable
    p1_set_name = input("What is the first player's name? ")
    p1_set_token = input(f"What token will {p1_set_name} be? ")
    p2_set_name = input("What is the second player's name? ")
    p2_set_token = input(f"What token will {p2_set_name} be? ")
    # uses those variables with player class to save into variables
    p1 = Player(p1_set_name,p1_set_token)
    p2 = Player(p2_set_name,p2_set_token)
    print(f"Player '{p1.token}' is {p1.name}, and Player '{p2.token}' is {p2.name}")

    # sets a turn count and starts the REPL
    turn_count = 0
    while True:
        # uses turn count to determin whose turn it is
        if turn_count % 2 == 0:
            player_turn = p1
        else:
            player_turn = p2
        # asks the players for the row and column they wish to put their token
        row_turn = int(input(f"{player_turn.name}, which row will you put your {player_turn.token}? (top to bottom, 1-3) "))
        column_turn = int(input(f"{player_turn.name}, which column will you place your {player_turn.token}? (left to right, 1-3) "))
        # puts the token in the designated spot
        Game.move(column_turn,row_turn,player_turn.name)
        # shows the game board
        print(Game())
        #adds to the turn counter
        turn_count += 1
        # checks for win conditions. if met, prints winner and ends game
        if Game.calc_winner() == "win":
            print(f'Tic Tac Toe! {player_turn.name} wins!')
            break
        # checks if board is full. if true, ends game
        if Game.is_full() == "game_over":
            print("Board is full. Game over.")
            break

main()

