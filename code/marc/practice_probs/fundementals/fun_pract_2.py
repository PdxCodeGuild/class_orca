# practice 2 for fundementals
# positive AND negative interger
def pos_and_neg (a,b):
    if a < 0 and b >= 0 or b < 0 and a >= 0 :
        return True
    else:
        return False
# print(pos_and_neg(2,2))
# print(pos_and_neg(-2,-2))
# print(pos_and_neg(-2,2))
print(pos_and_neg(2,-2))