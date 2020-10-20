def cat_dog(x):
    cat_count = x.count('cat')
    dog_count = x.count('dog')
    if cat_count == dog_count:
        return True
    else:
        return False

def main():
    user_input = input('Enter a string to see if it contains the same amount of "cats" as "dogs": ')

    print(cat_dog(user_input))

main()