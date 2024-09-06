message = "A kong string with a silly typo"
# message[2] = "l"
# TypeError: 'str' object does not support item assignment

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

pets = "Cats & Dogs"
# pets.index("x")
# This will throw an error
# ValueError: substring not found

pets = "Cats & Dogs"
print("Dragons" in pets)  # False
print("Cats" in pets)  # True


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


email = "myothet@gmail.com"
old_domain = "gmail.com"
new_domain = "solidplm.com"
new_email = replace_domain(email, old_domain, new_domain)
print(new_email)
