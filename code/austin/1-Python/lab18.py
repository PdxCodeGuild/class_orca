#Lab18: Peaks and Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_list = []
valley_list = []
final_list = []

#returns index of item that has lower number on right and left
def peaks():
    for i in range(1, len(data) - 1):
        if data[i] > data[i + 1] and data[i] > data[i - 1]:
            peak_list.append(data[i])
    print(peak_list, "peaks")
peaks()

#returns index of item that ha higher number on right and left
def valleys():
    for i in range(1, len(data) - 1):
        if data[i] < data[i + 1] and data[i] < data[i - 1]:
            valley_list.append(data[i])
    print(valley_list, "valleys")
valleys()

#compiles a list of peaks and valleys in order of appearance
def peaks_and_valleys():
    for i in range(1, len(data) - 1):
        if data[i] > data[i + 1] and data[i] > data[i - 1]:
            final_list.append(data[i])
        if data[i] < data[i + 1] and data[i] < data[i - 1]:
            final_list.append(data[i])
    print(final_list)
peaks_and_valleys()





