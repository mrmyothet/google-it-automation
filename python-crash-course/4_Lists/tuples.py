fullname = ("Grace", "M", "Hopper")
print(fullname)


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
print(result)
print(type(result))

# Unpacking
hours, minutes, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)

# Strings - sequences of characters; immutable
# Lists - sequences of elements of any type; mutable
# Tuples - Sequences of elements of any type; immutable

# The position of the elements inside the tuple have meaning

result = 5000 / 3600
print(result)  # 1.3888888888888888

result = 5000 // 3600
print(result)  # 1


# Let's use tuples to store information about a file:
# its name, its type and its size in bytes.
def file_size(file_info):
    file_name, file_type, size = file_info
    return "{:.2f}".format(size / 1024)


print(file_size(("Class Assignment", "docx", 17875)))  # Should print 17.46
print(file_size(("Notes", "txt", 496)))  # Should print 0.48
print(file_size(("Program", "py", 1239)))  # Should print 1.21


# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple,
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)
print(type(my_tuple))

# Tuples with mutable objects
my_tuple = (1, 2, ["a", "b", "c"])
print(my_tuple)
# my_tuple[0] = 3
# TypeError: 'tuple' object does not support item assignment

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = "x"
print(my_tuple)


# Returning multiple values from functions
def calculate_numbers(a, b):
    return a + b, a - b, a * b, a / b


result = calculate_numbers(10, 2)
print(result)

add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)
print(sub_result)
