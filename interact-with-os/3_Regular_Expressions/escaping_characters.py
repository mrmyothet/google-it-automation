import re

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))


# Check if the text passed has at least 2 groups of alphanumeric characters
# including letters, numbers, and underscores) separated by
# one or more whitespace characters
def check_character_groups(text):
    result = re.search(r"[a-zA-Z0-9_]+\s+[a-zA-Z0-9_]+", text)
    return result != None


print(check_character_groups("One"))
print(check_character_groups("123 Ready Set GO"))
print(check_character_groups("username user_01"))
print(check_character_groups("shopping_list: milk, bread, eggs"))
