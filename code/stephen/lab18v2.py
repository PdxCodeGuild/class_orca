
# iterate through a list of data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# when value is lower on both sides = peak
def peaks(data):
    peaks_list = []
    for i in range(1, len(data)-1):
        if data[i + 1] < data[i] > data[i-1]:
            peaks_list.append(i)
            
    print(peaks_list)
# when value is higher on both sides, valley
def valleys(data):
    valleys_list = []
    for i in range(1, len(data)-1):
        if data[i + 1] > data[i] < data[i - 1]:
            valleys_list.append(i)
        
    print(valleys_list)
# assign peaks and valleys into seperate list in the order they occur
def peaks_and_valleys(data):
    p_v_list = []
    for i in range(1, (len(data)-1)):
        if data[i + 1] < data[i] > data[i-1]:
            p_v_list.append(i)
        elif data[i + 1] > data[i] < data[i - 1]:
            p_v_list.append(i)
    print(p_v_list)
    

def drawing_x(data):
    draw_list = []
    for i in range(len(data)):
        sides = 'x' * data[i]
        draw_list.append(sides)
    
    for i in zip(*draw_list):
        print(i)

    # print(draw_list)



peaks(data)
valleys(data)
peaks_and_valleys(data)
drawing_x(data)


