single = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}

tens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

def digit():
    dig =''

    while dig != 'exit':
        dig = input('Enter number 0 thru 99 or type "exit"  ').lower()

        if dig == 'exit':
            break
        elif dig == '':
            return digit()
        
        dig = int(dig)
        s_dig = int(dig%10)
        t_dig = int(dig//10)
        
        if dig in range(0,100):
            if dig >= 0 and dig < 10:
                phrase = single[dig]
            elif dig > 9 and dig < 20:
                phrase = tens[dig]
            elif t_dig != 0 and s_dig == 0:
                phrase = tens[t_dig]
            else:
                phrase = tens[t_dig] + ' ' + single[s_dig]
            print(phrase.capitalize())
            return digit()
        else:
            return digit()

digit()