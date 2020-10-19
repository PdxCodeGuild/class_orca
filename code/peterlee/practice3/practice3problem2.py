def main():
    lst = []
    while True:
        user_input = input('Enter a number (or "done"): ')
        if user_input == 'done':
            print(lst)
            break
        else:
            lst.append(user_input)

main()

'''
1
2
3
4
5
6
7
8
9
done
['1', '2', '3', '4', '5', '6', '7', '8', '9']
'''