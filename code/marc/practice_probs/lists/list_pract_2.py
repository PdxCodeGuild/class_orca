# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

# eveneven([5, 6, 2]) → True
# eveneven([5, 5, 2]) → False


def even_even(some_list_of_ints):
    evens = [num for num in some_list_of_ints if num % 2 == 0]
    if len(evens) % 2 == 0:
        return True

    else:
        return False

num_list = [2,46,8,7,5,12]

print(even_even(num_list))

    