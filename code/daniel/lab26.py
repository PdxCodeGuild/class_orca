class Player:

    def __init__(self, name, token):
        
        self.name = name
        self.token = token

class Game:
    
    def __init__(self):
        
        self.board = [ [], [], [] ], [ [], [], [] ], [ [], [], [] ]

    def __repr__(self):
        '''Returns a pretty print out of the board game. '''
        self.turn_board = f'''
        {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}
        {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}
        {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}
        '''
        return self.turn_board

    def move(self, x, y, token):
        
        while True:
            if self.board[x][y] == []:
                self.board[x][y] = token
                break
            else:
                print("Spot already taken")
                x = int(input('Enter horizontal position: '))
                y = int(input('Enter vertical position: '))
        
    def cal_winner(self, token):
    
        i = 0
        for x in range(0,3):
            if self.board[x][i] == self.board[x][i+1] == self.board[x][i+2] == token:
                return True
        for x in range(0,3):
            if self.board[i][x] == self.board[i+1][x] == self.board[i+2][x] == token:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == token:
            return True    
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] == token:
            return True
        else:
            return False

    def is_full(self):

        for item in self.board:
            for x in item:
                if x == []:
                    return False

    def is_game_over(self):

        if board_full != False or is_winner != False:
            return True
        
user = Game()

player_1 = Player('Player 1', 'X')
player_2 = Player('Player 2', 'O')

print("Enter you horizontal and verticle positions using 0-2 starting at top-left.")
print(repr(user))
# making moves
counter = 0
while True:
    
    if counter % 2 == 0:
        player = player_1
    else:
        player = player_2
    
    x = int(input(f'{player.name}, enter horizontal position: '))
    y = int(input(f'{player.name}, enter vertical position: '))
    user.move(x, y, player.token)
    counter += 1

    print(repr(user))

    board_full = user.is_full()
    if board_full != False:
        print("Cat's game!")
    
    is_winner = user.cal_winner(player.token)
    if is_winner == True:
        print(f"{player.name} wins!")
 
    game_over = user.is_game_over()
    if game_over == True:
        print('Game over!')
        break