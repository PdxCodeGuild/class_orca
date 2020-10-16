data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

x = len(data)
y = 9

new_list = []
for i in range(y):
    for n in range(x):
        q = data[n] + i
        if q <= 8:
            new_list.append(' ')
        else:
            new_list.append('X')
        

new_list = [new_list[i:i+21] for i in range (0, len(new_list), 21)]

for i in range(len(new_list)):
    print(new_list[i])

