# map(function, iterables) --> map object


def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]
sqrs_of_numbers = map(square, numbers)
print(sqrs_of_numbers)  # map object
print(list(sqrs_of_numbers))

for sqrs in sqrs_of_numbers:
    print(sqrs)

# print(next(sqrs_of_numbers))
# print(next(sqrs_of_numbers))
# print(next(sqrs_of_numbers))
# print(next(sqrs_of_numbers))
# print(next(sqrs_of_numbers))
# print(next(sqrs_of_numbers))


# Map with Lambda Expression
print()

sqrs_of_numbers = map(lambda x: x * x, numbers)

for number in sqrs_of_numbers:
    print(number)

# Map with Built-in Function

bases = [10, 20, 30, 40, 50]
index = [1, 2, 3, 4, 5]
powers = list(map(pow, bases, index))
print(powers)
