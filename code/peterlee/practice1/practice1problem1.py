def is_even(a):
    if a%2 == 1:
        return False
    else:
        return True

def main():
    number = int(input('Enter an integer to find out if it is even: '))
    print(is_even(number))

main()

#5 -> False
#6 -> True
