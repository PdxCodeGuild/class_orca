'''
Lab 18: Peaks and Valleys
Version 2
Matthew Chimenti
'''


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peak = []
valley = []
counter = 0
largest_num = 0

for i in range(1, len(data) - 1):
    counter += 1
    # print(i)
    # print(data)
    if data[i] > data[i - 1] and data[i] > data[i + 1]:
        # print(counter)
        # print(data[i])
        # print('peak')
        peak.append(counter)
    elif data[i] < data[i - 1] and data[i] < data[i + 1]:
        # print(counter)
        # print(data[i])
        # print('valley')
        valley.append(counter)

peak_and_valley = peak + valley

# for i in range(1, len(data) - 1):
for b in data:
    if b > largest_num:
      largest_num = b
# print(largest_num)




for y in range(largest_num, 0, -1):
    for x in range(len(data)):
        if data[x] < y:
            print(' ', end='')
        elif data[x] >= y:
            print('x', end='')
    print()



