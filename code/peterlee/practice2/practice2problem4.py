def count_hi(x):
    return x.count('hi')

def main():
    user_input = input('Enter a string to count the number of times "hi" occurs in it: ')
    print(count_hi(user_input))

main()