def near_100(a):
    if abs(a - 100) <= 10:
        return True
    else:
        return False

def main():
    number = int(input('Enter a number. '))
    print(f'Is this number near 100? {near_100(number)}')

main()

