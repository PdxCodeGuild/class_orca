import random

def random_element(a):
    return a[random.randint(0, 2)]

def main():
    fruits = ['apples', 'bananas', 'pears']
    print(random_element(fruits))

main()

#apples
#pears