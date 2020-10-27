def latest_letter(x):
    y = list(x)
    y.sort()
    return y.pop()

def main():
    user_input = input('Enter a string of letters: ')
    print(latest_letter(user_input))

main()
    
