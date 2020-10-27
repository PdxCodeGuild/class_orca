def opposite(a, b):
    if a * b < 0:
        return True
    else:
        return False

def main():
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    
    print(f'Are these integers opposites? {opposite(a, b)}')

main()

#1, 2, -> False
#-1, 2 -> True
