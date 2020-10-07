nums = [5, 0, 8, 3, 4, 1, 6]
sum = 0

# # loop over the elements
# for num in nums:
#     print(num)

# loop over the indices
# for i in range(0, len(nums), 1):
#     sum += nums[i]
#     print(nums[i])
#     print(sum)
#     avg = sum / len(nums)
#     print(avg)


#Version 2
nums = []
avg = 0

def find_avg(nums):
    sum = 0
    for i in range(0, len(nums), 1):
        sum += nums[i]
    avg = sum / len(nums)

    print(f'Your average is {round(avg, 2)}')
    return 


while True:
    grade = input("Enter a number: ")
    if grade == "done":
        print(nums)
        find_avg(nums)
        break
    nums.append(int(grade)) 

