# Skill Group 1
# Iterate over the key and value pairs of a dictionary
# using a for loop with the dictionary.items() method
# to calculate the sum of the values in a dictionary.


# This function returns the total time, with minutes represented as
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day.
def sum_server_use_time(Server):
    total_use_time = 0.0

    for key, value in Server.items():
        total_use_time += Server[key]

    return round(total_use_time, 2)


FileServer = {
    "EndUser1": 2.25,
    "EndUser2": 4.5,
    "EndUser3": 1,
    "EndUser4": 3.75,
    "EndUser5": 0.6,
    "EndUser6": 8,
}

print(sum_server_use_time(FileServer))


# Skill Group 2
# Concatenate a value, a string, and the key for each item in the dictionary
# and append to the end of a new list[ ] using the list.append(x) method.

# Iterate over keys with multiple values from a dictionary using nested for loops
# with the dictionary.items() method.


def list_full_names(employee_dictionary):
    full_names = []

    for last_name, first_names in employee_dictionary.items():
        for first_name in first_names:
            full_names.append(first_name + " " + last_name)

    return full_names


employee_dict = {
    "Ali": ["Muhammad", "Amir", "Malik"],
    "Devi": ["Ram", "Amaira"],
    "Chen": ["Feng", "Li"],
}
print(list_full_names(employee_dict))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']

# Skill Group 3
# Use the dictionary[key] = value operation to associate a value with a key in a dictionary.

# Iterate over keys with multiple values from a dictionary,
# using nested for loops and an if-statement, and the dictionary.items() method.

# Use the dictionary[key].append(value) method to add the key, a string,
# and the key for each item in the dictionary.


def invert_resource_dict(resource_dictionary):
    new_dictionary = {}

    for resource_group, resources in resource_dictionary.items():
        for resource in resources:
            if resource in new_dictionary:
                new_dictionary[resource].append(resource_group)
            else:
                new_dictionary[resource] = [resource_group]

    return new_dictionary


resources = {
    "Hard Drives": ["IDE HDDs", "SCSI HDDs"],
    "PC Parts": ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"],
    "Video Cards": ["High-end video cards", "Basic video cards"],
}
print(resources)
print(invert_resource_dict(resources))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}

# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# https://www.w3schools.com/python/python_dictionaries.asp
