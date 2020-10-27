def missing_char(x):
    lst = []
    for i in range(len(x)):
        lst.append(x[0:i]+x[i+1:len(x)])
    return lst


def main():
    user_input = input('Enter a word: ')

    print(missing_char(user_input))

main()