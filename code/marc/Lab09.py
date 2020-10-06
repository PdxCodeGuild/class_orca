# This is the unit converter lab
def main():
    # this is version one
    # x = input("What is the distance in feet?:\n")
    # x = int(x)
    # print(f"{x} feet is equal to {x * .3048} meters")
    # version 2
    # x = input("What is the distance?:\n")
    # x = int(x)
    # y = input("What is the unit: ft, mi, m or km?:\n")
    # if y == "ft":
    #     print(f"{x} {y} is equal to {x * .3048} meters")
    # elif y == "mi":
    #     print(f"{x} {y} is equal to {x * 1609.34} meters")
    # elif y == "m":
    #     print(f"{x} {y} is equal to {x} meters")
    # elif y == "km":
    #     print(f"{x} {y} is equal to {x * 1000} meters")
    # else:
    #     print("Cannot compute with what you entered.")

    #version 3
    # x = input("What is the distance?:\n")
    # x = int(x)
    # y = input("What is the unit: in, ft, y, m, km, or mi?:\n")
    # if y == "ft":
    #     print(f"{x} {y} is equal to {x * 0.3048} meters")
    # elif y == "mi":
    #     print(f"{x} {y} is equal to {x * 1609.34} meters")
    # elif y == "m":
    #     print(f"{x} {y} is equal to {x} meters")
    # elif y == "km":
    #     print(f"{x} {y} is equal to {x * 1000} meters")
    # elif y == "in":
    #     print(f"{x} {y} is equal to {x * 0.0254} meters")
    # elif y == "y":
    #     print(f"{x} {y} is equal to {x * 0.9144} meters")
    # else:
    #     print("Cannot compute with what you entered.")
    
    #version 4

    x = input("What is the distance?:\n")
    x = int(x)
    y = input("What is the input unit: in, ft, y, m, km, or mi?:\n")
    z = input("What is the output unit: in, ft, y, m, km, or mi?:\n")
    if y == "in":
        meters = x * 0.0254
    elif y == "ft":
        meters = x * 0.3048
    elif y == "mi":
        meters = x * 1609.34
    elif y == "m":
        meters = x * 1
    elif y == "km":
        meters = x * 1000
    elif y == "y":
        meters = x * 0.9144
    # else:
    #     print("Cannot compute with what you entered.")
    #     #exit()
        
    if z == y:
        output = x * 1
    elif z == "in":
        output = meters / 0.0254
    elif z == "ft":
        output = meters / 0.3048
    elif z == "mi":
        output = x / 1609.34
    elif z == "m":
        output = x / 1
    elif z == "km":
        output = x / 1000
    elif z == "y":
        output = x / 0.9144
    print(f"{x} {y} is equal to {output} {z}.")
    # else:
    #     print("Cannot compute with what you entered.")
    #     #exit()
       
    
 
    # else:
    # print("Cannot compute with what you entered.")
       
main()