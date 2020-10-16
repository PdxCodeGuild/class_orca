powers_of_2 = [2**x for x in range(10)]

# print(powers_of_2)

ten_evens = [x for x in range(19) if x % 2 == 0]

# print(ten_evens)
dict1 = {1: 'one', 2: 'two'}
kvswap = {value:key for key, value in dict1.items()}

# print(kvswap)

import string
a = {}
b = {a.update(x) for x, ord(x) in string.ascii_lowercase}

print(a)