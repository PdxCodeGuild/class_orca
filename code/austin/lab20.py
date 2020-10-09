#Credit Card Validation

# cc = '5555888899991235'
cc = '1234555567892345'

# cc = input("Please enter a 16-digit credit card number ")

if len(cc) < 16:
        cc = input("That is not a valid number. Please enter 16 digits: ")

def cc_validate(cc):

    cc_ints = list(cc)
    print(cc_ints)

    cc_ints = [int(num) for num in cc]
    print(cc_ints)

    slice1 = slice(15,16)
    check = cc_ints[slice1]
    print(check, "check digit")

    slice3 = slice(-1)
    cc_ints = cc_ints[slice3]
    print(cc_ints, "THIS IS THE NEW CARD NUMBER")

    reversed_cc_ints = cc_ints[::-1]
    print(reversed_cc_ints, "reversed cc")

    doubled_list = []

    for i in range(0, len(reversed_cc_ints), 1):
        if i % 2 == 0:
            doubled_ints = reversed_cc_ints[i] * 2
            doubled_list.append(doubled_ints)
        else:
            doubled_list.append(reversed_cc_ints[i])
    print(doubled_list, "doubled values")
    
    for i in range(0, len(doubled_list), 1):
        if doubled_list[i] > 9:
            doubled_list[i] = doubled_list[i] - 9
    print(doubled_list, "subtract 9")

    cc_sum = sum(doubled_list)
    print(cc_sum)

    check_digit = [int(y) for y in str(cc_sum)]
    print(check_digit, "check digits")

    if check_digit[1] == check:
        print("Credit card is valid")
    else:
        print("Credit card is not valid")


cc_validate(cc)
