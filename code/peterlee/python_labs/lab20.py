#function for doubling every other element in the list
def double(lst):
    new_list = lst
    for x in range(15):
        if x % 2 == 0:
            new_list[x] = new_list[x] * 2
    return new_list

#function for subtracting 9 from numbers over 9
def subtract_nine(lst):
    new_list_two = lst
    for x in range(15):
        if new_list_two[x] > 9:
            new_list_two[x] -= 9
    return new_list_two

def main():
    card = input('Enter a credit card number, without spaces, to check its validation: ')

    #converts string input into a list of ints
    card_list = [int(x) for x in card]

    print(f'1. {card_list}')

    #holds check_digit for last step
    check_digit = card_list.pop(15)

    print(f'2. {card_list}')

    card_list_reversed = list(reversed(card_list))

    print (f'3. {card_list_reversed}')


    card_list_doubled_every_other = double(card_list_reversed)

    print(f'4. {card_list_doubled_every_other}')


    card_list_subtract_nine = subtract_nine(card_list_doubled_every_other)

    print(f'5. {card_list_subtract_nine}')

    #sums and converts the list to a string so we can split it later
    card_list_sum = str(sum(card_list_subtract_nine))

    print(f'6. {card_list_sum}')

    #splits the sum to pop the second digit
    card_list_sum_split = [int(x) for x in card_list_sum]
    second_digit = card_list_sum_split.pop(1)

    print(f'7. {second_digit}')

    if second_digit == check_digit:
        print('8. Valid!')
    else:
        print('8. Not Valid!')

main()