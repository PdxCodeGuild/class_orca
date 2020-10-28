#1

def is_even(a):
    if a % 2 == 0:
        return True
    elif a % 2 == 1:
        return False

# print(is_even(11))

def opposite(a, b):
    if a < 0 and b > 0:
        return True
    if a > 0 and b < 0:
        return True
    if a > 0 and b > 0:
        return False
    if a < 0 and b < 0:
        return False

# print(opposite(-3, -4))

def near100(num):
    if num in range(90,111):
        return True
    if num < 90:
        return False
    if num > 110:
        return False
    
# print(near100(110))


def maximum_of_three(a, b, c):
    if (a >= b) and (a >= c):
        return a
    if (b >= a) and (b >= c):
        return b
    if (c >= a) and (c >= b):
        return c

# print(maximum_of_three(13,4,15))

def powers_of_two():
    nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for x in nums:
        print(2 ** x)

powers_of_two()