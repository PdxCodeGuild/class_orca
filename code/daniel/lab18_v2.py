
lst = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# def peak_vs_valley(lst):
#     peaks = []
#     valleys = []
    
#     for item in range(1, len(lst)-1):
#         if lst[item-1] < lst[item] > lst[item+1]:
#             peaks.append(item) 

#         elif lst[item-1] > lst[item] < lst[item+1]:
#             valleys.append(item)
#     return peaks, valleys

# def main():
#     results = peak_vs_valley(lst)
#     peaks, valleys = results
#     len_peak = len(peaks)
#     len_valley = len(valleys)
#     print(f'''
#     Data set: {lst}
#     There are {len_peak} peaks in the data set. Their indices are: {peaks}.
#     There are {len_valley} valleys in the data set. Their indices are: {valleys}.
#     '''
#     )
# main()

