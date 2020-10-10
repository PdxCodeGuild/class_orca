
def main():
    def card_valid(a = "y"):
        c_card = input("Please input your 16 digit credit card, ommiting all spaces:\n")
        while len(c_card) != 16:
            c_card = input("Invalid card length, try again:\n")
        c_card_chars = list(c_card) 
        c_card_nums = [int(c_card_chars[num]) for num in range(16)]
        print (c_card_nums)
        check_num = c_card_nums.pop(15)
        print (f"The check number is:\n{check_num}")
        c_card_15 = c_card_nums[0:15]
        print(c_card_15)
        c_card_rev = c_card_15[::-1]
        print(c_card_rev)
        c_card_rev_dbl = [c_card_rev[num] * 2 if num % 2 == 0 else c_card_rev[num] for num in range(15)]
        print (c_card_rev_dbl)
        c_card_dbl_minus_9 = []
        for i in range (15):
            if c_card_rev_dbl[i] > 9:
                c_card_dbl_minus_9.append((c_card_rev_dbl[i] - 9))
            else:
                c_card_dbl_minus_9.append(c_card_rev_dbl[i])
        print(c_card_dbl_minus_9)
        sum_total = sum(c_card_dbl_minus_9)
        print(sum_total)
        ver_num = (sum_total % 10)
        print (ver_num)
        if check_num == ver_num:
            message = "This card is valid, time to go shopping on the black market."
        else:
            message = "This card is not valid. Time to steal more purses."
        return message
    
    a = input ("Would you like to validate a credit card? y or n:\n")
    while a != "y" and a != "n":
        a = input("y or n:\n")
    if a == "y":
        print (card_valid("y"))
    elif a == "n":
        print("Too bad, 'cause that's all I do man!")
        return
    
        


main()