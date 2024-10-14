import re


def check_sentence(text):
    result = re.search(r"^[A-Z][a-z\s]*[.|?|!]$", text)
    return result != None


print(check_sentence("Is this is a sentence?"))
print(check_sentence("is this is a sentence?"))
print(check_sentence("Hello"))
print(check_sentence("1-2-3-GO!"))
print(check_sentence("A star is born."))
