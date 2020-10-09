# this is list comprension practice 2
# Write a comprehension to generate the first 10 even numbers.

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def even_nums(a, b = 0):
    even_values = [num for num in range(b, a+1) if num %2 == 0]
    return even_values
print(even_nums(40, 1))