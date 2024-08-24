str = "Greetings, Earthlings"
print(str)  # Greetings, Earthlings
print(str[0])  # G
print(str[:])  # Greetings, Earthlings
print(str[4:8])  # ting
print(str[11:])  # Earthlings
print(str[-10:])  # Earthlings
print(str[:5])  # Greet

# If your index is beyond the end of the string,
# Python returns an empty string.
print(str[55:])  # ""


# An optional way to slice an index is by the stride argument, indicated by using a double colon.
# This allows you to skip over the corresponding number of characters in your index,
# or if you’re using a negative stride, the string prints backwards.

print(str[::])  # Greetings, Earthlings
print(str[::-1])  # sgnilhtraE ,sgniteerG

# To join strings in Python, you use the plus operator, + ,
print("Hello" + " " + "World")

# You can also use the join() function,
# when you want to concatenate elements from a list of strings with a specific delimiter.
greetings = ["Hello", "World"]
print(" ".join(greetings))


# combine slicing and joining strings
# 2025551212
def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line


phone_number = "2025551212"
print(phone_number)
print(format_phone(phone_number))
