import random


def linear_search(list, key):
    """
    if key is in the list returns its position in the list,

    otherwise returns -1
    """
    no_of_comparison = 0

    for i, item in enumerate(list):

        if item == key:
            print("No. of comparison", no_of_comparison)
            return i

        no_of_comparison += 1

    return -1


list = [random.randint(0, 100) for _ in range(100)]
key = random.randint(0, 100)

print("list: ", list)
print("key: ", key)

print("found position: ", linear_search(list, key))
