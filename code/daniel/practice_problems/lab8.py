monies = int(input("Enter a number of pennies:  "))

quarters = monies // 25
print(quarters)

dimes = (monies % 25) // 10
print(dimes)

nickles = (monies % 25) // 5
print(nickles)

squares = [num**2 for num in range(10)]
# variable = ['new value' 'old value' 'range']

# list comprehension is best suited for simple transformations
# otherwise aim for readability and use a loop for more complex transformations
