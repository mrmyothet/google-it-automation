# len(string) - Returns the length of the string
print(len("abcde"))  # 5

# for character in string - Iterates over each character in the string
for c in "abcde":
    print(c)

# if substring in string - Checks whether the substring is part of the string
print("abc" in "abcde")  # True
print("def" in "abcde")  # False

# string[i] - Accesses the character at index i of the string, starting at zero
print("abcde"[2])  # c
print("abcde"[-1])  # e


# string[i:j] - Accesses the substring starting at index i, ending at index j minus 1.
# If i is omitted, its value defaults to 0.
# If j is omitted, Python returns everything from i to the end of the string.
print("abcde"[0:2])  # ab
print("abcde"[2:])  # cde


# String methods

# string.lower() - Returns a copy of the string with all lowercase characters
print("AaBbCcDdEe".lower())  # aabbccddee

# string.upper() - Returns a copy of the string with all uppercase characters
print("AaBbCcDdEe".upper())  # AABBCCDDEE

# string.lstrip() - Returns a copy of the string with the left-side whitespace removed
print("  Hello  ".lstrip())

# string.rstrip() - Returns a copy of the string with the right-side whitespace removed
message = "   Hello   "
print(message.rstrip())

# string.strip() - Returns a copy of the string with both the left and right-side whitespace removed
print(message.strip())

# string.count(substring)- Returns the number of times substring is present in the string
test = "How much wood would a woodchuck chuck"
print(test.count("wood"))

# string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.
print("12345".isnumeric())  # True
print("-123.45".isnumeric())  # False

# string.isalpha() - Returns True if there are only letters in the string. If not, returns False.
print("xyzzy".isalpha())

# string.split() - Returns a list of substrings that were separated by whitespace
# (whitespace can be a space, tab, or new line)
print(test.split())

# string.split(delimiter) - Returns a list of substrings that were separated by whitespace or another string
test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))

# string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.
print(test.replace("wood", "plastic"))

# delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter
print("-".join(test.split()))
