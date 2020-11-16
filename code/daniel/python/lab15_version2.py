'''
Daniel Eggimann
PDX Code Guild
Lab 15
'''

''' Version  '''
hundreds_list = ['', 'one-hundred', 'two-hundred', 'three-hundred', 'four-hundred', 'five-hundred', 'six-hundred', 'seven-hundred', 'eight-hundred', 'nine-hundred']
base_list = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
aux_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
weird_nums_list = ['ten', 'eleven', 'twelve', 'thirteen'] 
teens_list = ['teen']

def diminish_nums(num):
    hundreds_num = num // 100 
    base_num = num // 10 % 10
    aux_num = num % 10
    return hundreds_num, base_num, aux_num

def convert_hundreds(hundreds):
    return hundreds_list[hundreds]

def convert_base(base_num):
    return base_list[base_num]

def convert_aux(aux_num):
    return aux_list[aux_num]

def convert_weird_nums(aux_num):
    if aux_num < 4:
        return weird_nums_list[aux_num]
    elif aux_num > 3:
        if aux_num == 5:
            return 'fifteen'
        return aux_list[aux_num] + teens_list[0]

def main():
    raw_num = int(input('Enter a number:  '))
    hundreds_num, base_num, aux_num = diminish_nums(raw_num)
    if hundreds_num > 0:
        hundreds_word = convert_hundreds(hundreds_num)
        base_word = convert_base(base_num)
        aux_word = convert_aux(aux_num)
        if base_num != 0 and aux_num != 0:
            print(hundreds_word + '-' + base_word + '-' + aux_word)
        elif base_num == 0 and aux_num != 0:
            print(hundreds_word + '-' + aux_word)
        elif base_num != 0 and aux_num == 0:
            print(hundreds_word + '-' + base_word)
    elif base_num == 0:
        aux_word = convert_aux(aux_num)
        print(aux_word)
    elif base_num == 1:
        weird_nums = convert_weird_nums(aux_num)
        print(weird_nums)
    elif base_num > 1:
        base_word = convert_base(base_num)
        aux_word = convert_aux(aux_num)
        if aux_num == 0:
            print(base_word + aux_word)
        elif aux_num != 0:
            print(base_word + '-' + aux_word)

main()


