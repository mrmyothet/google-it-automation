# List Comprehensions
# Let us create new lists based on sequences or ranges

# For loop
# Iterates or repeats over a sequence of values

multiples = []
for x in range(1, 11):
    multiples.append(x * 7)

print(multiples)


multiples = [x * 7 for x in range(1, 11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0, 100) if x % 3 == 0]
print(z)


# The odd_numbers function returns a list of odd numbers between 1 and n
def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []
