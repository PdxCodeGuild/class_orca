
game_board ={
    "r1": [" "," "," "],
    "r2": [" "," "," "],
    "r3": [" "," "," "]
}

class Player:
    def __init__(self,name,token):
        self.name = name 
        self.token = token
        # player = f'{name},{token}'

class Game:
    global p1
    global p2
    def init (self,board):
        self.board = game_board

    def move(x,y,player):
        if player == p1.name: # confirmed is pulling input value of p1 and p2
            game_board[f'r{y}'][int(x)-1] = p1.token
            return game_board
        else:
            game_board[f'r{y}'][int(x)-1] = p2.token
            return game_board

    def __repr__ (self):
        disp_board = f"""{game_board["r1"][0]}|{game_board["r1"][1]}|{game_board["r1"][2]}
{game_board["r2"][0]}|{game_board["r2"][1]}|{game_board["r2"][2]}
{game_board["r3"][0]}|{game_board["r3"][1]}|{game_board["r3"][2]}"""
        return disp_board

    def calc_winner():
        for key,value in game_board.items():
            check = value[0]
            for i in value:
                if i == check:
                    result = True
                if i != check:
                    result = False
                    break
            if result = False:
                pass
            else:
                print(f"Tic Tac Toe! {i} wins!")

    def is_full():
        full = True
        for key,value in game_board.items()
            for i in value:
                if i == " ":
                    full = False
        print(full)

    def is_game_over():      

        

def main():
    global p1
    global p2
    p1_set_name = input("What is the first player's name? ")
    p1_set_token = input(f"What token will {p1_set_name} be? ")
    p2_set_name = input("What is the second player's name? ")
    p2_set_token = input(f"What token will {p2_set_name} be? ")
    p1 = Player(p1_set_name,p1_set_token)
    p2 = Player(p2_set_name,p2_set_token)
    print(f"Player '{p1.token}' is {p1.name}, and Player '{p2.token}' is {p2.name}")


    move = Game.move(2,2,'joe')
    move1 = Game.move(1,1,'jax')



    # this works
    # y =2
    # x = 2
    # game_board[f'r{str(y)}'][int(x)-1] = p1.token
    # print(game_board)

 
main()

