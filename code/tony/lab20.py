N = 16

def checker():
    cc_in = input(f'Input CC number ({N} digits) '  ).replace(' ','')
    credit = [int(x) for x in cc_in]
    if len(credit) == N:   #if input is N numbers
        check = credit[-1]                              # save check digit
        print(credit)
        credit.pop()                                    # remove last digit
        print(credit)
        credit = credit[::-1]                           # reverse digits
        print(credit)
        credit[::2] = [x*2 for x in credit[::2]]        # for ever other number, x*2
        print(credit)
        credit = [x-9 if x > 9 else x for x in credit]  # subtract 9 from numbers > 9
        print(credit)
        credit = sum(credit)%10                         # add digits, then get second digit
        print(credit)
        if credit == check:        # if second digit matches check digit
            print('Valid!')
        else:                   # if digits don't match
            print('Invalid!')
        print(credit)
    else:                   # if input is not N numbers
        print('Try again \n')
        return checker()

checker()