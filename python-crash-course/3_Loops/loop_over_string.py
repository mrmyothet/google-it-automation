print("Looping over a string")

greeting = "Hello"
for char in greeting:
    print(char)


for i in range(len(greeting)):
    print(i)


print("while loop with indexing")

greeting = "Hello"
index = 0
while index < len(greeting):
    print(greeting[index])
    index += 1

print("while loop with slicing")

greeting = "Hello"
index = 0
while index < len(greeting):
    print(greeting[index : index + 1])
    index += 1

print("List comprehensions")

numbers = [1, 2, 3, 4, 5]
squared_number = [x**2 for x in numbers]
print(numbers)
print(squared_number)
