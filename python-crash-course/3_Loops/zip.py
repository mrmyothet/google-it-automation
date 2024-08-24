# Python zip() Method
# The zip() method takes one or more iterables (such as list, tuple, string, etc.)
# and constructs the iterator of tuples where each tuple contains elements from each iterable.

# zip(*iterables)


numbers = [1, 2, 3]
str_numbers = ["One", "Two", "Three"]
result = zip(numbers, str_numbers)
print(result)  # <zip object>
print(list(result))  # [(1, 'One'), (2, 'Two'), (3, 'Three')]

# Any number of iterables can be passed as arguement in the zip() method.

numbers = [1, 2, 3]
str_numbers = ["One", "Two", "Three"]
roman_numbers = ["I", "II", "III"]
result = zip(numbers, str_numbers, roman_numbers)
print(result)
print(list(result))

# The zip object can be cast to a list of tuples.
# Each tuple will have corresponding elements from both list parameters.

teams = ["India", "England", "NZ", "Aus"]
captains = ["Kohli", "Root", "Williamson", "Smith"]
zipped = zip(teams, captains)
zipped_list = list(zipped)
print("zipped list ")
print(zipped_list)

# It can also be cast to a dictionary.

teams = ["India", "England", "NZ", "Aus"]
captains = ["Kohli", "Root", "Williamson", "Smith"]
zipped = zip(teams, captains)
zipped_dict = dict(zipped)
print("zipped_dict : ")
print(zipped_dict)

# Since the zip object is an iterator,
# it can be traversed with the next() function until the StopIteration exception is reached.

teams = ["India", "England", "NZ", "Aus"]
captains = ["Kohli", "Root", "Williamson", "Smith"]
zipped = zip(teams, captains)
while True:
    try:
        tup = next(zipped)
        print(tup[0], "->", tup[1])
    except StopIteration:
        break

# But what if the iterable parameters are not equal in length?

java = "Java"
python = "Python"
php = "PHP"
print(list(zip(java, python, php)))
# [('J', 'P', 'P'), ('a', 'y', 'H'), ('v', 't', 'P')]

import itertools

print(list(itertools.zip_longest(java, python, php)))
# [('J', 'P', 'P'),
# ('a', 'y', 'H'),
# ('v', 't', 'P'),
# ('a', 'h', None),
# (None, 'o', None), (
# None, 'n', None)]

# Instead of None, any other character can be specified as fillvalue parameter.

print(list(itertools.zip_longest(java, python, php, fillvalue="?")))
# [('J', 'P', 'P'),
# ('a', 'y', 'H'),
# ('v', 't', 'P'),
# ('a', 'h', '?'),
# ('?', 'o', '?'),
# ('?', 'n', '?')]

# The zip() function proves useful in cases like parallel traversal and sorting of lists.
items = ["book", "keyboard", "pen", "mounse"]
price = [325, 500, 75, 250]
sorted_list = sorted(list(zip(price, items)))
print(sorted_list)
# [(75, 'pen'), (250, 'mounse'), (325, 'book'), (500, 'keyboard')]

# Another application of the zip() function is
# when corresponding values of lists have to be used in some processing.
sales = [2500, 15000, 7800, 5000]
rates = [15, 10, 8, 10]
combined = list(zip(sales, rates))
for s, r in combined:
    gst = s * r / 100
    print("sales:{} rate:{} GST:{}".format(s, r, gst))

# Unzipping Zip Object
# Python doesn't have a separate function for unzipping a zipped object in separate tuples.
# The zip() function itself, when used with * (the unpacking operator),
# is used for unzip operation.
digits = [1, 2, 3, 4, 5]
words = ["one", "two", "three", "four", "five"]
zip_obj = zip(digits, words)

# to unzip
x, y = zip(*zip_obj)
print(x)  # (1, 2, 3, 4, 5)
print(y)  # ('one', 'two', 'three', 'four', 'five')
