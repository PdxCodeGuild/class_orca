def lower_case(x):
    lowered = x.lower()
    return lowered.strip()

def main():
    user_input = input('Enter a string you want to make lower case and clear of white spaces: ')
    print(lower_case(user_input))

main()