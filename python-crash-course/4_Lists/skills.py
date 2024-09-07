# Skill Group 1

# Use a for loop to modify elements of a list.
# Use the list.append() method.
# Use the string.endswith() and string.replace() methods to modify the elements within a list.

years = [
    "January 2023",
    "May 2025",
    "April 2023",
    "August 2024",
    "September 2025",
    "December 2023",
]

updated_years = []

for year in years:
    if year.endswith("2023"):
        new = year.replace("2023", "2024")
        updated_years.append(new)
    else:
        updated_years.append(year)

print(updated_years)

# Skill Group 2
# Use a list comprehension to return values


def squares(start, end):
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Skill Group 3

# Use a list comprehension to modify elements of a list.
# Use the string.replace() method within a list comprehension.
# Use the string[index] method within a list comprehension.

years = [
    "January 2023",
    "May 2025",
    "April 2023",
    "August 2024",
    "September 2025",
    "December 2023",
]

updated_years = [
    year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years
]
print(updated_years)

# Skill Group 4

# Use the string.split() method to separate a string into a list of individual words.
# Iterate over the new list using a for loop.
# Modify each element in the list by slicing the element’s string at a given [1:] index position and appending the substring to the end of the element.
# Convert a list back into a string.


def change_string(given_string):
    new_string = ""
    new_list = given_string.split()

    for element in new_list:
        new_string += element[1:] + "-" + element[0] + " "

    return new_string


print(change_string("1one 2two 3three 4four 5five"))
# Should print "one-1 two-2 three-3 four-4 five-5"


# Skill Group 5
# Use the string.join() method to concatenate a string that provides a list name and its elements.
def list_elements(list_name, elements):
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(
    list_elements(
        "Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]
    )
)
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"


# Skill Group 6
# Use map() and convert the map object to a list so we can print all the results at once.


# A simple function to add 1 to a given number
def add_one(number):
    return number + 1


# A list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
result = map(add_one, numbers)

# Convert the map object to a list to print the result
print(list(result))

# Skill Group 7
# Use zip() to combine a list of names and ages into a list of tuples,
# and print all the tuples at once.

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

combined = zip(names, ages)
print(list(combined))

# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# https://docs.python.org/3/library/stdtypes.html#lists
# https://docs.python.org/3/library/stdtypes.html#tuples
