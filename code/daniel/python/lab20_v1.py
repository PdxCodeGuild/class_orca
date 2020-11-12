user_input = input('Enter your 16-digit credit card number:  ')
user_list = list(user_input)
user_list = [int(num) for num in user_list]
check_digit = user_list.pop(15)
user_list.reverse()

for num in range(0, 15, 2):
    if num % 2 == 0:
        user_list[num] = user_list[num] * 2

for num in range(len(user_list)):
    if user_list[num] > 9:
        user_list[num] -= 9
num_sum = 0
for num in range(len(user_list)):
    num_sum += user_list[num]

num_sum = str(num_sum)
num_sum = list(num_sum.strip())
print(num_sum[-1])
validation_digit = num_sum.pop(-1)
validation_digit = int(validation_digit)
if validation_digit == check_digit:
    print('Valid!')
else:
    print('Not Valid!')



