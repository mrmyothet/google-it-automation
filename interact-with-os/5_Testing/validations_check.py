from validations import validate_user

result = validate_user("", -1)
print(result)

result = validate_user("myuser", 1)
print(result)

# result = validate_user(88, 1)
# print(result)

# result = validate_user([], 1)
# print(result)

# result = validate_user(["name"], 1)
# print(result)
