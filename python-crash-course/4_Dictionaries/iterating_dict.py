file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

for extension in file_counts:
    print(extension)

for ext, count in file_counts.items():
    print("There are {} files with the .{} extension".format(count, ext))

keys = file_counts.keys()
values = file_counts.values()

print(type(keys))
print(keys)

print(type(values))
print(values)

for value in file_counts.values():
    print(value)


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


count_1 = count_letters("aaaaa")
count_2 = count_letters("tenant")
count_3 = count_letters("a long string with a lot of letters")

print(count_1)
print(count_2)
print(count_3)

cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for cool, beast in cool_beasts.items():
    print("{} have {}".format(cool, beast))


# Check if a key exists in the dictionary and perform different actions
# based on the result

key = "banana"
myDictionary = {"banana": 3}
if key in myDictionary:
    print(f"The value of {key} is {myDictionary[key]}")
else:
    print(f"{key} is not found in the dictionary")
