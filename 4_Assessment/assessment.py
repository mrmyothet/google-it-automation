def confirm_length(word):

    # Complete the condition statement using a string operation.
    if len(word) > 0:
        # Complete the return statement using a string operation.
        return len(word)
    else:
        return 0


print(confirm_length("a"))  # Should print 1
print(confirm_length("This is a long string"))  # Should print 21
print(confirm_length("Monday"))  # Should print 6
print(confirm_length(""))  # Should print 0


def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for char in string:
        # Complete the if-statement using a string method.
        if char.isalpha():
            count_alpha += 1
    return count_alpha


print(alpha_length("This has 1 number in it"))  # Should print 17
print(alpha_length("Thisisallletters"))  # Should print 16
print(alpha_length("This one has punctuation!"))  # Should print 21


def alphabetize_lists(list1, list2):

    new_list = []  # Initialize a new list.
    list1.extend(list2)  # Combine the lists.
    list1.sort()  # Sort the combined lists.
    new_list = list1  # Assign the combined lists to the "new_list".
    return new_list


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']


def even_numbers(first, last):
    return [num for num in range(first, last) if num % 2 == 0]


print(even_numbers(4, 14))  # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]


def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items
    # in the dictionary.
    for continent, countries in countries_dict.items():
        # Use a string method to format the required string.
        result += "{} \n".format(countries)
    return result


print(
    countries(
        {
            "Africa": ["Kenya", "Egypt", "Nigeria"],
            "Asia": ["China", "India", "Thailand"],
            "South America": ["Ecuador", "Bolivia", "Brazil"],
        }
    )
)

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']


def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {}  # Initialize a new dictionary
    for guest in guest_list:  # Iterate over the elements in the list
        result[guest] = 0  # Add each list element to the dictionary as a key with
        # the starting value of 0
    return result


guests = [
    "Adam",
    "Camila",
    "David",
    "Jamal",
    "Charley",
    "Titus",
    "Raj",
    "Noemi",
    "Sakira",
    "Chidi",
]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}


def setup_gradebook(old_gradebook):
    # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook = old_gradebook.copy()
    # Complete the for loop to iterate over the new gradebook.
    for student in old_gradebook.keys():
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[student] = 0
    return new_gradebook


fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])


music_genres = ["rock", "pop", "country"]
music_genres.append("blues")
print(music_genres)


teacher_names = {
    "Math": "Aniyah Cook",
    "Science": "Ines Bisset",
    "Engineering": "Wayne Branon",
}
print(teacher_names.values())
