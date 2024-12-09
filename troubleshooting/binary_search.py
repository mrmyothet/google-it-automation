import random


def binary_search(list, key):
    """
    Returns the position of key in the list if found, -1 otherwise

    list must be sorted
    """
    left = 0
    right = len(list) - 1

    no_of_comparison = 0

    while left <= right:
        middle = (left + right) // 2
        # a // b the quotient of a divided by b, rounded to the next smallest whole number

        if list[middle] == key:
            print("No. of comparison:", no_of_comparison)
            return middle

        if list[middle] > key:
            right = middle - 1

        if list[middle] < key:
            left = middle + 1

        no_of_comparison += 1

    return -1


list = [random.randint(0, 100) for _ in range(100)]
key = random.randint(0, 100)

# print('unsorted list:', list)

list = sorted(list)

print("list: ", list)
print("key: ", key)

print("found position: ", binary_search(list, key))
