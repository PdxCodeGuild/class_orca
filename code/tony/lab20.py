N = 16

def checker():
    cc_in = input(f'Input CC number ({N} digits) '  ).replace(' ','')
    credit = [int(x) for x in cc_in]
    if len(credit) == N:   #if input is N numbers
        check = credit[-1]                              # save check digit
        credit.pop()                                    # remove last digit
        credit = credit[::-1]                           # reverse digits
        credit[::2] = [x*2 for x in credit[::2]]        # for ever other number, x*2
        credit = [x-9 if x > 9 else x for x in credit]  # subtract 9 from numbers > 9
        credit = sum(credit)%10                         # add digits, then get second digit
        if credit == check:        # if second digit matches check digit
            print('Valid!')
        else:                   # if digits don't match
            print('Invalid!')
    else:                   # if input is not N numbers
        print('Try again \n')
        return checker()

checker()