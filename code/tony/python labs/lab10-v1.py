# v1
# ---------
nums = [5, 0, 8, 3, 4, 1, 6]
for L in nums:
    print(L)
list_total = len(list(nums))
sum_total = sum(list(nums))
print(f'number of numbers: {list_total}')
print(f'sum of numbers: {sum_total}')

average = sum_total / list_total
print(f'average of numbers: {average}')