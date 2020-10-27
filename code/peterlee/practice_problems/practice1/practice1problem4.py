def maximum_of_three(a, b, c):
    max_list = [a, b, c]
    max_list.sort()
    return max_list[2]

def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    c = int(input("Enter a third number: "))

    print(f'The maximum of these numbers is {maximum_of_three(a, b, c)}')

main()

#1, 2, 3 -> 3
#5, 9, 3 -> 9