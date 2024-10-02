file = open("sample_data/spider.txt")
print(file.readline())
print(file.readline())

print(file.read())
file.close()

# open - use - close

with open("sample_data/spider.txt") as file:
    print(file.read())

with open("sample_data/spider.txt") as file:
    for line in file:
        print(line.upper())

with open("sample_data/spider.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("sample_data/spider.txt")
lines = file.readlines()
file.close()

print(lines)
print(type(lines))

lines.sort()
print(lines)
