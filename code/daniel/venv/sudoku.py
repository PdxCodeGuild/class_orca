
import random 

class Sudoku:
    
    def __init__(self):
        '''Initiate sudoku'''
        # lists of numbers
        self.columns = [ [], [], [], [], [], [], [], [], [] ]
        self.blocks = [ [], [], [], [], [], [], [], [], [] ]
        self.sudoku_nums = [ ]

    def block_mkr(self, x):
        '''Distribute numbers into 3x3 blocks'''
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
        '''Generate unique rows with digits 1-9'''
        digits = [1,2,3,4,5,6,7,8,9]
        random.shuffle(digits)
        # while True:
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
            # break
        return digits

    def make_board(self):
        '''Attaches unique string of digits to specified list.'''
        counter = 0
        for x in range(0,9):
            self.new_row = self.make_row(x)
            while self.new_row == False:
                self.new_row = self.make_row(x)
                counter += 1
            self.block_mkr(x)
            for i in range(0,9):    
                self.columns[i].append(self.new_row[i])
            self.sudoku_nums.append(self.new_row)
        print(counter) 

    def strip_nums(self):
        '''Strip numbers from sudoku board'''
        copy_sudoku_nums = self.sudoku_nums
        rand_nums = [ ] 
        rand_nums.append(copy_sudoku_nums[3][3]) 
        copy_sudoku_nums[3][3] = ''
        print(rand_nums) 

    def print_board(self):
        '''Initiates sudoku board contructions and returns completed board'''
        self.make_board()
        self.strip_nums()
        for row in self.sudoku_nums:
            print(row)
        return self.sudoku_nums

def main():
    sudoku = Sudoku()
    sudoku.print_board() 

if __name__=='__main__':
    main()