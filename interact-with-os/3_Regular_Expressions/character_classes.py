import re

print(re.search(r"[pP]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "what a way to go"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats"))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats"))
print(re.findall(r"cat|dog", "I like both dogs and cats"))
