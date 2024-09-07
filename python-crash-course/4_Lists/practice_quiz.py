filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename[:-2])
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = [
    filename[:-2] if filename.endswith("hpp") else filename for filename in filenames
]  # Start your code here


print(new_filenames)
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# Create a function that turns text into pig latin.
# Pig latin is a simple text transformation that modifies each word by:
# moving the first character to the end of each word;
# then appending the letters "ay" to the end of each word.
# For example, python ends up as ythonpay.
def pig_latin(text):
    say = ""
    lst = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say = word[1:] + word[0] + "ay"
        lst.append(say)
        # Turn the list back into a phrase
    return " ".join(lst)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(
    pig_latin("programming in python is fun")
)  # Should be "rogrammingpay niay ythonpay siay unfay"


def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples.
    for person in people:

        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"
        name, age, profession = person

        # Format the required sentence and place the 3 variables
        # in the correct placeholders using the .format() method.
        print("{} is {} years old and works as {}".format(name, age, profession))


# Call to the function:
biography_list(
    [("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")]
)


# Click Run to submit code


# Output should match:
# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer
