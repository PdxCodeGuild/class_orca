#Credit Card Validation

# cc = '5555888899991235'
cc = '4556737586899855'

cc = input("Please enter a 16-digit credit card number ")

if len(cc) < 16:
        cc = input("That is not a valid number. Please enter 16 digits: ")

def cc_validate(cc):

    #Step 1:
    cc_ints = list(cc)
    print(cc_ints)

    cc_ints = [int(num) for num in cc]
    print(cc_ints, "cc integers")

    #Step 2: Check digit
    slice1 = slice(15,16)
    check = cc_ints[slice1]
    print(check, "check digit")

    slice3 = slice(-1)
    cc_ints = cc_ints[slice3]
    print(cc_ints, "THIS IS THE NEW CARD NUMBER")

    #Step 3: Reverse
    reversed_cc_ints = cc_ints[::-1]
    print(reversed_cc_ints, "reversed cc")

    #Step 4: Double every other element
    doubled_list = []

    for i in range(0, len(reversed_cc_ints), 1):
        if i % 2 == 0:
            doubled_ints = reversed_cc_ints[i] * 2
            doubled_list.append(doubled_ints)
        else:
            doubled_list.append(reversed_cc_ints[i])
    print(doubled_list, "doubled values")
    
    #Step 5: Subtract if over 9
    for i in range(0, len(doubled_list), 1):
        if doubled_list[i] > 9:
            doubled_list[i] = doubled_list[i] - 9
    print(doubled_list, "subtract 9")

    #Sum all values
    cc_sum = sum(doubled_list)
    print(cc_sum)

    check_digit = [int(y) for y in str(cc_sum)]
    print(check_digit, "check digits")

    if check_digit[1] == check[0]:
        print("Credit card is valid")
    else:
        print("Credit card is not valid")

    print(check[0], "check digit")
    return check[0] == check_digit[1]

cc_validate(cc)
