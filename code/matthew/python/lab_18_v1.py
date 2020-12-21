'''
Lab 18: Peaks and Valleys
Version 2
Matthew Chimenti
'''


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peak = []
valley = []
counter = 0


# for i in range(21):
#     print(i)

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
print(f'The indices of the peaks are: {peak}')
print(f'The indices of the valleys are: {valley}')
print(f'The indices for peak and valleys are: {peak_and_valley}')