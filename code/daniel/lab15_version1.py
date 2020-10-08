'''
Daniel Eggimann
PDX Code Guild
Lab 15
'''

''' Version 1 '''

base_list = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
aux_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
weird_nums_list = ['ten', 'eleven', 'twelve', 'thirteen'] 
teens_list = ['teen']

def diminish_nums(num):
    base_num = num // 10
    aux_num = num % 10
    return base_num, aux_num

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
    base_num, aux_num = diminish_nums(raw_num)
    if base_num == 0:
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


