try:
    f = open("/etc/hosts", "w+")
except IOError as ex:
    print("Error appending to file: " + str(ex))
else:
    f.close()


### Avoiding defensive code with exceptions
user = {}

# instead of doing this:
if isinstance(user, dict) and "first_name" in user:
    first_name = user["first_name"]

# Do this instead:
try:
    first_name = user["first_name"]
except KeyError:
    print("User does not have a first_name field")
