''' Practice Problem 1 '''
# Write a function that tells whether a number is even or odd

# def is_even(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'

# num1 = 12345
# num2 = 23450897
# num3 = 32454

# first_num = is_even(num1)
# second_num = is_even(num2)
# third_num = is_even(num3)
# print(f'{num1} is {first_num}, {num2} is {second_num}, {num3} is {third_num}')


''' Practice Problem 2 '''
# Write a function that takes two ints, a and b, and returns True if one is 
# positive and the other is negative.

# def is_positive(num1, num2):
#     if num1 >= 0 and num2 < 0:
#         return True
#     elif num1 < 0 and num2 >= 0:
#         return True
#     else:
#         return False
# def main():
#     first_num = int(input('Enter a positive or negative number:  '))       
#     second_num = int(input('Enter a postive or negative number:  '))
#     results = is_positive(first_num, second_num)
#     print(results)

# main()


''' Practice Problem 3 '''
# Write a function that returns True if a number within 10 of 100.

# def range(number):
#     if (100 - number) < 10:
#         return True
#     else: 
#         return False

# def main():
#     num = int(input(f"Enter a number:  "))
#     print(f'That number is within 10 digits of 100:  {range(num)}')

# main()


''' Practice Problem 4 '''
# write a function that returns the maximum of 3 parameters

# def determine_max(num1, num2, num3):
#     return max(num1, num2, num3)

# def main():
#     print('Enter three numbers to see which one isthe greatest')
#     first_num = int(input('First number:  '))
#     sec_num = int(input('Second number:  '))
#     third_num = int(input('Third number:  '))
#     print(f'The greatest number is {determine_max(first_num, sec_num, third_num)}.')

# main()


''' Practice Problem 5 '''
# Print out the powers of 2 from 2^0 to 2^20

# def raise_to_power(num):
#     powers_list = []
#     count = 0
#     while count <= 20:
#         powers_list.append(str(num ** count))
#         count +=1
#     return powers_list

# def main():
#     print('Enter a number to see something cool:  ')
#     number = int(input(':  '))
#     results = raise_to_power(number)
#     results = ', '.join(results)
#     print(results)

# main()


