import random

def eveneven(a):
    new_list = []
    for x in a:
        if x % 2 == 0:
            new_list.append(x)
    if len(new_list) % 2 == 0:
        return True
    else:
        return False

def main():
    lst = []
    for q in range(random.randint(0, 99)):
        lst.append(random.randint(0, 99))
    print(lst)
    print(eveneven(lst))

main()

# [58, 70, 80, 73, 8, 53, 40, 5, 19, 55, 76, 46, 26, 49, 98, 2, 83, 79, 62, 72, 8, 24]
# True

# [99, 45, 33, 54, 19, 80, 20, 12, 61, 56, 84, 1, 67, 38]
# False