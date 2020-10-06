# # Lab Ten "Average Numbers"
# # version 1
# def main():
#     nums = [5, 0, 8, 3, 4, 1, 6]
#     i = 0
#     sum = 0
# # loop over the elements
#     for num in nums:
#         sum  = sum + nums[i]
#         i += 1
#     average = sum/len(nums)
#     #print(sum)
#     #print (len(nums))
#     print(f"The average of the list is {average}")

# version 2
def main():

    nums = []
    i = 0
    sum = 0

    while True:
        new_num = input("Enter a number or type 'done':\n")
        if new_num == "done":
            break
        else:
            new_num = int(new_num)
            nums.append(new_num)

    for num in nums:
        sum  = sum + nums[i]
        i += 1
    average = sum/len(nums)
    
    print (f"Here is your list:{nums}\n")
    print (f"Here is the sum of your list:{sum}\n")
    print(f"The average of the list is {average}")

main()