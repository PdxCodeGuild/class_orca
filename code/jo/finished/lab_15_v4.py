
# dictionaries to pull the numbers from
spell_hour = {1: 'one',2: 'two',3: 'three',4: 'four',5: 'five',6: 'six',7: 'seven',8: 'eight',9: 'nine',10: 'ten',11: 'eleven',12: 'twelve'}

spell_tens = {2: 'twenty',3: 'thirty',4: 'forty',5: 'fivety',0: 'zero'}

spell_singles = {1: 'one',2: 'two',3: 'three',4: 'four',5: 'five',6: 'six',7: 'seven',8: 'eight',9: 'nine'}

spell_teens = {10: 'ten',11: 'eleven',12: 'twelve',13: 'thirteeyn',14: 'fourteen',15: 'fifteen',16: 'sixteen',17: 'seventeen',18: 'eighteen',19: 'nineteen'}

# gets time from user
time = input("What time is it? 'HH:MM'")

# converts the time to a list, then splits and converts to int to print hour and evaluate min
split_time = time.split(":")
hour = int(split_time[0])
minute = int(split_time[1])

# evaluates minutes to send to print
if 10 <= minute <= 19:
    minute = spell_teens[minute]
elif minute <= 9:
    minute = spell_singles[minute]
elif 20 <= minute <= 99:
    tens_digit = (minute//10)
    ones_digit = (minute%10)
    if ones_digit == 0:
        minute = f"{spell_tens[tens_digit]}"
    else:
        minute = f"{spell_tens[tens_digit]}{spell_singles[ones_digit]}"

# prints hour and minute
print(f"The time is {spell_hour[hour]} {minute}")