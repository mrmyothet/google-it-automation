import re

result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(result)

result = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(result)

result = re.sub(
    r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"
)
print(result)


result = re.sub(r"^([\w .-]*), ([\w .-]*)", r"\2 \1", "Lovelace, Ada")
print(result)

result = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(result)
