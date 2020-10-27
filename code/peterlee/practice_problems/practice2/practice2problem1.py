def double_letters(a):
    for x in a:
        a = a.replace(x, x+x)
    return a
    
def main():
    string = input("Enter a string: ")
    result = double_letters(string)

    print(result)

main()

#asdf -> aassddff