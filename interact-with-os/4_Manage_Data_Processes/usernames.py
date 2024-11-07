usernames = {}

name = "good user"

usernames[name] = usernames.get(name, 0) + 1
print(usernames)

usernames[name] = usernames.get(name, 0) + 1
print(usernames)
