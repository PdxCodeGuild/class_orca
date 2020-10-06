nums = []

while True:
    add = input("enter a number, or 'done': ")
    if add == 'done':
        break
    nums.append(int(add))

average = sum(nums) / len(nums)

print(f'average: {average}')
