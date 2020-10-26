
import random 

class Sudoku:
    
    def __init__(self):

        self.columns = [ [], [], [], [], [], [], [], [], [] ]

        self.blocks = [ [], [], [], [], [], [], [], [], [] ]

        self.sudoku_nums = [ ]

    def block_mkr(self, x):

        if 0 <= x < 3:

            for i, num in enumerate(self.new_row):

                if i < 3:

                    self.blocks[0].append(num)

                if 2 < i < 6:

                    self.blocks[1].append(num)

                if 5 < i < 9:

                    self.blocks[2].append(num)

        elif 2 < x < 6:

            for i, num in enumerate(self.new_row):

                if i < 3:

                    self.blocks[3].append(num)

                elif 2 < i < 6:

                    self.blocks[4].append(num)

                elif 5 < i < 9:

                    self.blocks[5].append(num)

        elif 5 < x < 9:

            for i, num in enumerate(self.new_row):

                if i < 3:

                    self.blocks[6].append(num)

                elif 2 < i < 6:

                    self.blocks[7].append(num)

                elif 5 < i < 9:

                    self.blocks[8].append(num)

    def make_row(self, z):

        digits = [1,2,3,4,5,6,7,8,9]
        
        random.shuffle(digits)

        while True:

            for x, num in enumerate(digits):
                    
                    if num in self.columns[x]:

                        random.shuffle(digits) 

                        return False

                    elif 0 <= z < 3:

                        if 0 <= x < 3:

                            if num in self.blocks[0]:

                                random.shuffle(digits) 

                                return False

                        elif 3 <= x < 6:

                            if num in self.blocks[1]:

                                random.shuffle(digits) 

                                return False
                        
                        elif 6 <= x < 9:

                            if num in self.blocks[2]:

                                random.shuffle(digits) 

                                return False

                    elif 3 <= z < 6:

                        if 0 <= x < 3:

                            if num in self.blocks[3]:

                                random.shuffle(digits) 

                                return False

                        elif 3 <= x < 6:

                            if num in self.blocks[4]:

                                random.shuffle(digits) 

                                return False
                        
                        elif 6 <= x < 9:

                            if num in self.blocks[5]:

                                random.shuffle(digits) 

                                return False

                    elif 6 <= z < 9:

                        if 0 <= x < 3:

                            if num in self.blocks[6]:

                                random.shuffle(digits) 

                                return False

                        elif 3 <= x < 6:

                            if num in self.blocks[7]:

                                random.shuffle(digits) 

                                return False
                        
                        elif 6 <= x < 9:

                            if num in self.blocks[8]:

                                random.shuffle(digits) 

                                return False

            break

        return digits

    def make_board(self):
        counter = 0
        for x in range(0,9):
        
            self.new_row = self.make_row(x)
            
            while self.new_row == False:
                
                self.new_row = self.make_row(x)
                counter += 1
            self.block_mkr(x)

            self.sudoku_nums.append(self.new_row)

            for i in range(0,9):    

                self.columns[i].append(self.new_row[i])

        print(counter) 

    def print_board(self):

        print('\nSudoku\n')
        block = self.sudoku_nums
        x = 0
        z = 0

        for row in block:
            print(row)

        # for x in range(z, (z+3)):

        #     print(f'| {block[x][0]}  {block[x][1]}  {block[x][2]} | {block[x][3]}  {block[x][4]}  {block[x][5]} | {block[x][6]}  {block[x][7]}  {block[x][8]} |')
        #     print(f'| {block[x+1][0]}  {block[x+1][1]}  {block[x+1][2]} | {block[x+1][3]}  {block[x+1][4]}  {block[x+1][5]} | {block[x+1][7]}  {block[x+1][7]}  {block[x+1][8]} |')
        #     print(f'| {block[x+2][0]}  {block[x+2][1]}  {block[x+2][2]} | {block[x+2][3]}  {block[x+2][4]}  {block[x+2][5]} | {block[x+2][6]}  {block[x+2][7]}  {block[x+2][8]} |')
        #     print('\n') 
        #     x += 3  
        #     z += 3      

sudoku = Sudoku()
sudoku.make_board()
sudoku.print_board()
# print(sudoku.blocks) 