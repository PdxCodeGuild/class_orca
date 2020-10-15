def peaks(a):
    new_list_peaks = []
    for x in range(len(a) - 1):
        y = a[x]
        if y > a[x+1] and y > a[x-1]:
            new_list_peaks.append(x)
    return new_list_peaks
def valleys(b):
    new_list_valleys = []
    for x in range(1, len(b) - 1):
        y = b[x]
        if y < b[x+1] and y < b[x-1]:
            new_list_valleys.append(x)
    return new_list_valleys

def peaks_and_valleys(c, d):
    new_list_pv = c + d
    return new_list_pv

    

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def main():
    peaks_list = peaks(data)
    valleys_list = valleys(data)
    peaks_and_valleys_list = peaks_and_valleys(peaks_list, valleys_list)
    peaks_and_valleys_list_sorted = sorted(peaks_and_valleys_list)

    print(f'data = {data}')
    print(f'peaks = {peaks_list}')
    print(f'valleys = {valleys_list}')
    print(f'peaks and valleys = {peaks_and_valleys_list_sorted}')
main()