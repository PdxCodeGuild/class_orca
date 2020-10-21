# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

# def random_element(a):
#     ...

# fruits = ['apples', 'bananas', 'pears']
# random_element(fruits) could return 'apples', 'bananas' or 'pears'
from random import randint
def random_element(a):
    what_fruit = a[randint(0,(len(a)-1))]
    return what_fruit

the_list = ["goog", "gorp", "glank", "gleevo"]

print(random_element(the_list))