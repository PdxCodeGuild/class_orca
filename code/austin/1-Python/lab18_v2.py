#Lab18 version 2: ASCII Peaks and Valleys

import matplotlib.pyplot as plt 

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
x = []
y = []


def draw_graph():
    x_val = 0
    y_val = 0

    #x axis values 
    for i in data:
        x_val = x_val + 1
        x.append(x_val)
    print(x, "x list")


    y = [num for num in data]
    print(y, "y list")

    # plot and draw coordinates
    plt.plot(x, y)

    plt.xlabel('x axis: position in list') 

    plt.ylabel('y axis: value') 
    
    plt.title('Peaks and Valleys') 
    
    plt.show() 


draw_graph()





