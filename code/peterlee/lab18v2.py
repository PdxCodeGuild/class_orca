def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

    x = len(data)
    y = 9
    #creates a list that show where blank spaces and X's need to go 
    new_list = []
    for i in range(y):
        for n in range(x):
            q = data[n] + i
            if q <= 8:
                new_list.append(' ')
            else:
                new_list.append('X')
            
    #separates the list into multiple lists where each list signifies a horizontal line
    new_list = [new_list[i:i+21] for i in range (0, len(new_list), 21)]

    #prints the proper X's and blank spaces for each number in [data]
    for x in range(9):
        space = ' '
        print(space+'  '.join(new_list[x]))
    print(data)

main()