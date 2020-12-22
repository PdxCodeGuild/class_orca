'''
Lab 10
Version 1
Matthew Chimenti
'''


# nums = [5, 0, 8, 3, 4, 1, 6]
# number = 0
# sum = 0
#
# for num in nums:
#     number += num
#
# sum = number / (len(nums))
# print(sum)

'''
Lab 10
Version 2
'''

nums = []
number = 0
sum = 0

while True:
    entered_number = input("enter a number, or 'done' ")
    if entered_number == "done":
        break
    nums.append(int(entered_number))

for num in nums:
    number += num
sum = number / (len(nums))
print(f"average: {sum}")
