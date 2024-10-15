import re


def rearrange_name(name):
    pattern = r"^(\w*), (\w*)$"
    result = re.search(pattern, name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))


def rearrange_name2(name):
    pattern = r"^([\w \.-]*), ([\w \.-]*)$"
    result = re.search(pattern, name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


print(rearrange_name2("Hopper, Grace M."))
print(rearrange_name2("Kennedy, John F."))
