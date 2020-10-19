#Fundamentals

#1
def is_even(a):
    if a % 2 == 0:
        return True
# print(is_even(5)) 
# print(is_even(6)) 

#2
def opposite(a, b):
    if a > 0 and b < 0:
        return True
    if a < 0 and b > 0:
        return True
    else:
        return False
# print(opposite(10, -1)) 
# print(opposite(2, 3)) 
# print(opposite(-1, -1))

#3 
def near_100(num):
    if num >= 90 and num <= 110:
        return True
    else: 
        return False

# print(near_100(50)) 
# print(near_100(99))
# print(near_100(105)) 

#4
def maximum_of_three(a, b, c):
    max = 0
    if a > max:
        max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max
# print(maximum_of_three(5,6,2)) 
# print(maximum_of_three(-4,3,10))

#5
def exponents():
    for i in range(0,20):
        i += 1
        series = 2**i
        print(series, "2^", i)

exponents()
