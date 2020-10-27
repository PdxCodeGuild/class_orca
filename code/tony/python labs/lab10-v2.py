nums = []
tack = ''

while tack != 'done':
    tack = input('Enter a number or "Done"  ').lower()
    try:
        nums.append(float(tack))
    except:
        print('Input number')
    
    if tack == 'done':
        list_total = len(nums)
        # print(nums)
        print(list_total)
        sum_total = sum(nums)
        print(sum_total)
        average = sum_total / list_total
        print(f'Average of these numbers is {average}')
        # print(nums)