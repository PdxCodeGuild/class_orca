# this is string practice 1
# double letter
def double_letter(a):
    double_list = []
    string_list = list(a)
    for i in string_list:
        double_list.append(i + i)
    
    double_word = "".join(double_list)
    print(double_word)
    return double_word
# print(double_letter("box"))
print (double_letter("tube"))




