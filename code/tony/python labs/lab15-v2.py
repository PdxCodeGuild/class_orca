single = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
tens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

def digit():
    dig =''
    
    while dig != 'exit':        # loops until 'exit' input. error on other string
        dig = input('Enter number 0 thru 999 or type "exit"  ').lower()

        if dig == 'exit':   # break on 'exit' input
            break
        elif dig == '':     # loop if accidental empty input
            return digit()

        dig = int(dig)          # main number
        dig_ = int(dig%100)     # to keep numbers over 100 and have number to evaluate that are under. 
        s_dig = int(dig_%10)    # 1s digit
        t_dig = int(dig_//10)   # 10s digit
        h_dig = int(dig//100)   # 100s digit

        def ten():
            phrase =''
            if dig_ in range(0,10):                 # below 10
                phrase = single[dig_]
            elif dig_ in range(10,20):              # uniques between 10 and 20
                phrase = tens[dig_]
            elif t_dig > 0 and s_dig == 0:          # multiples of 10
                phrase = tens[t_dig]
            else:                                   # anything over 20 and not multiple of 10 
                phrase = tens[t_dig] + ' ' + single[s_dig]
            return phrase.capitalize()

        p = ten()   # store phrase of anything under 100 into variable

        if dig in range(0,100):                     # just print under 100 phrase
            print(f'{p}\n')
            return digit()
        elif dig in range(100,1000):    # numbers over 100 go here
            if dig_ == 0:                           # to print multiples of 100
                print(f'{single[h_dig].capitalize()} hundred\n')
            else:                                   # prints any other number over 100
                print(f'{single[h_dig].capitalize()} hundred and {p}\n')
            return digit()
        else:                                       # loop inputs of 1000+
            return digit()

digit()