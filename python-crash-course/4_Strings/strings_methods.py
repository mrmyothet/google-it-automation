animals = "lions tigers and bears"
index_of_g = animals.index("g")
print(index_of_g)

animals = "lions tigers and bears"
index_of_bears = animals.index("bears")
print(index_of_bears)

animals = "lions tigers and bears"
is_there_horses = "horses" in animals
print(is_there_horses)  # False

animals = "lions tigers and bears"
tiger_in_animals = "tigers" in animals
print(tiger_in_animals)  # True

print("Mountains".upper())
print("Mountains".lower())

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

yes_strip = " yes ".strip()
print(yes_strip)

print(" yes ".strip())
print(" yes ".lstrip())
print(" yes ".rstrip())

e_count = "The number of times e occurs in this string is 4".count("e")
print(e_count)  # 4

print("Forest".endswith("rest"))
# True

print("Forest".isnumeric())  # False
print("12345".isnumeric())  # True

answer = int("12345") + int("54321")
print(answer)  # 66666

join_by_space = " ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
join_by_dots = "...".join(
    ["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]
)

print(join_by_space)
print(join_by_dots)

str_split = "This is another example".split()
print(str_split)
# ['This', 'is', 'another', 'example']

separated_by_comma = "Good Morning, this is another example include comma.".split(",")

answer = []
for s in separated_by_comma:
    temp = s.split()
    for s_temp in temp:
        answer.append(s_temp)

print(answer)
