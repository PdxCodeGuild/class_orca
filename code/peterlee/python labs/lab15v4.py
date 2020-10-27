hours = int(input('What is the current hour? '))
while hours > 12:
    hours = int(input('Please enter a valid hour from 1-12: '))
minutes = int(input('What is the current minute? '))
while minutes > 59:
    minutes = int(input('Please enter a valid minute from 0-59: '))

#converts hours and minutes to list indexes that can be used for their appropriate words
hours_converted = hours % 13
minutes_tens_digit = minutes // 10
minutes_ones_digit = minutes % 10

hours_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 
'eight', 'nine', 'ten', 'eleven', 'twelve']

minutes_tens_list = ['', '', 'twenty', 'thirty', 'fourty', 'fifty']

minutes_ones_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 
'seven', 'eight', 'nine']

minutes_other_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 
'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

if minutes == 0:
    print(f"It is {hours_list[hours_converted]} o'clock ")
elif minutes > 0 and minutes < 10:
    print(f"It is {hours_list[hours_converted]} oh {minutes_ones_list[minutes_ones_digit]}")
elif minutes > 9 and minutes < 20:
    print(f"It is {hours_list[hours_converted]} {minutes_other_list[minutes_ones_digit]}")
elif minutes > 19 and minutes_ones_digit == 0:
    print(f"It is {hours_list[hours_converted]} {minutes_tens_list[minutes_tens_digit]}")
else:
    print(f"It is {hours_list[hours_converted]} {minutes_tens_list[minutes_tens_digit]}-{minutes_ones_list[minutes_ones_digit]}")