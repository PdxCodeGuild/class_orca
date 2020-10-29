data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def find_peaks():
    peaks = []
    for i in range(len(data) - 1):
        if data[i-1] < data[i] > data[i+1]:
            peaks.append(i)
    return peaks

def find_valleys():
    valleys = []
    for i in range(len(data) - 1):
        if data[i-1] > data[i] < data[i+1] and i != 0:
            valleys.append(i)
    return valleys

def peaks_and_valleys():
    peaks_and_valleys = []
    for i in range(len(data) - 1):
        if data[i-1] < data[i] > data[i+1]:
            peaks_and_valleys.append(i)
        elif data[i-1] > data[i] < data[i+1] and i != 0:
            peaks_and_valleys.append(i)
    return peaks_and_valleys

print(find_peaks())
print(find_valleys())
print(peaks_and_valleys())






