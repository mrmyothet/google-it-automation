# Create a list of tuples where each tuple contains the numbers 1, 2, and 3.

numbers = [(1, 2, 3) for _ in range(5)]
print(numbers)

print("List comprehension result:")
result = [x * 2 for x in range(1, 11)]
print(result)

print("Long form code result:")
my_list = []
for x in range(1, 11):
    my_list.append(x * 2)
print(my_list)

# List comprehension with conditional statement
print("List comprehension result:")

result = [x for x in range(1, 101) if x % 10 == 0]
print(result)

print("Long form code result:")
my_list = []
for x in range(1, 101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)


# write a list comprehension to create a list of squared numbers (n*n or n**2).
# It needs to return a list of squares of consecutive numbers between “start” and “end” inclusively.
def squares(start, end):
    return [n**2 for n in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
