sequence = range(10)
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)

print(new_list)

print("*" * 15)

sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]

print(new_list)
