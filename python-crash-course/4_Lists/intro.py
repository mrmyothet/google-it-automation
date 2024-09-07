x = ["Now", "we", "are", "cooking!"]

print(type(x))
# <class 'list'>

print(x)
# ['Now', 'we', 'are', 'cooking!']

print(len(x))
# 4

print("are" in x)
# True

print("Today" in x)
# False

print(x[0])  # Now
print(x[3])  # cooking
# print(x[4])  # IndexError: list index out of range

print(x[1:3])  # ['we', 'are']
print(x[:2])  # ['Now', 'we']
print(x[2:])  # ['are', 'cooking!']


def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n - 1]
    return ""


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing

# In Python, lists and strings are quite similar.
# (1) being able to iterate over them using for loops;
# (2) support indexing;
# (3) using the len function to find the length of the sequence;
# (4) using the plus operator + in order to concatenate;
# (5) using the in keyword to check if the sequence contains a value.
