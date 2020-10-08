#Fundementals practice prob 4
# The maximum

# def the_max(a,b,c):
#     the_biggest = max(a,b,c)
#     return the_biggest
# print (the_max(6,5,7))

def the_max(a,b,c):
    if a > b and a > c:
        the_biggest = a
    if b > a and b > c:
        the_biggest = b
    if c > a and c > b:
        the_biggest = c
    return the_biggest
# print (the_max(6,5,7))
# print (the_max(25,5,7))
print (the_max(6,72,7))
