animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars / len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


result = full_emails(
    [("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]
)
print(result)


def skip_elements(elements):
    # code goes here
    result = []
    for index, element in enumerate(elements):
        if (index + 1) % 2 != 0:
            result.append(element)

    return result


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"]))
# Should be ['Orange', 'Strawberry', 'Peach']
