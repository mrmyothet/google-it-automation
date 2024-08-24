def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n:  # Complete the while loop condition
        if current_number % 2 == 0:
            count += 1  # Increment the appropriate variable
        current_number += 1  # Increment the appropriate variable
    return count


print(even_numbers(25))  # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000))  # Should print 501
print(even_numbers(0))  # Should print 1


print("#" * 30)

# Complete the range sequences in the nested loops so that “multiplication_table(1, 3)” will print:
# 1 2 3
# 2 4 6
# 3 6 9


def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(stop):
        # Complete the inner loop range
        for y in range(stop):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str((x + 1) * (y + 1)), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above


print("#" * 30)


# This function should count the number of values from 0 to the “max” parameter minus 1
# that are evenly divisible by the “divisor” parameter.
def divisible(max, divisor):
    count = 0  # Initialize an incremental variable
    for x in range(max):  # Complete the for loop
        if x % divisor == 0:
            count += 1  # Increment the appropriate variable
    return count


print(divisible(100, 10))  # Should be 10
print(divisible(10, 3))  # Should be 4
print(divisible(144, 17))  # Should be 9


print("#" * 30)

# This function should return a space-separated string of all odd positive numbers,
# up to and including the “maximum” variable that's passed into the function.
# Complete the for loop so that a function call like “odd_numbers(6)” will return the numbers “1 3 5”.


def odd_numbers(maximum):

    return_string = ""  # Initializes variable as a string

    # Complete the for loop with a range that includes all
    # odd numbers up to and including the "maximum" value.
    for number in range(maximum + 1):

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        if number % 2 != 0:
            return_string = return_string + str(number) + " "

    # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10))  # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed
