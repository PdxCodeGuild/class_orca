# This is first practice prob for list comprehensions
# Write a comprehension to generate the first 10 powers of two.

# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

def powers_of(x, a, b):
    ex_values = [x**num for num in range(a, b)]
    return ex_values
# print (powers_of(2,0,10))
print (powers_of(4,0,10))
# made it so the number you choose and the range are variables