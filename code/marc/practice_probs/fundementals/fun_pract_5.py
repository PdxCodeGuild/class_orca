#fundementals practice number 5

#the powers of 

def the_power_of (x, a, b):
    the_powers = []
    for i in range (a, b+1):
        exponent = x ** i
        the_powers.append(exponent)
    return the_powers
# print(the_power_of(2,0,20))
