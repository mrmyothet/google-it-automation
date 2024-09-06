# This function accepts a given string and checks each character of
# the string to see if it is a letter or not. If the character is a
# letter, that letter is added to the end of the string variable
# "forwards" and to the beginning of the string variable "backwards".
def mirrored_string(my_string):
    # Two variables are initialized as string data types using empty
    # quotes. The variable "forwards" will hold the "my_string"
    # minus any character that is not a letter. The "backwards"
    # variable will hold the same letters as "forwards", but in
    # in reverse order.
    forwards = ""
    backwards = ""

    # The for loop iterates through each character of the "my_string"
    for character in my_string:
        # The if-statement checks if the character is not a space.
        if character.isalpha():
            # If True, the body of the loop adds the character to the
            # to the end of "forwards" and to the front of
            # "backwards".
            forwards += character
            backwards = character + backwards

        # If False (meaning the character is not a letter), no action
        # is needed. This coding approach results prevents any
        # non-alphabetical characters from being written to the
        # "forwards" and "backwards" variables. The for loop will
        # restart until all characters in "my_string" have been
        # processed.

    if forwards.lower() == backwards.lower():
        return True
    return False


print(mirrored_string("12 Noon"))
print(mirrored_string("Was it a car or cat I saw"))
print(mirrored_string("eve, Madam Eve"))


def convert_weight(ounces):
    pounds = ounces / 16

    result = "{} ounces equals {:.2f} pounds".format(ounces, pounds)
    return result


print(convert_weight(12))
print(convert_weight(50.5))
print(convert_weight(16))


def username(last_name, birth_year):
    return "{}{}".format(last_name[0:3], birth_year)


print(username("Ivanov", "1985"))
print(username("Rodríguez", "2000"))
print(username("Deng", "1991"))


# This function checks a given schedule entry for an old date and, if
# found, the function replaces it with a new date.
def replace_date(schedule, old_date, new_date):

    # Check if the given "old_date" appears at the end of the given
    # string variable "schedule".
    if str(schedule).endswith(old_date):
        p = len(old_date)

        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
        return new_schedule

    return schedule


print(
    replace_date(
        "Last year’s annual report will be released in March 2023", "2023", "2024"
    )
)
print(replace_date("In April, the CEO will hold a conference", "April", "May"))
print(replace_date("The convention is scheduled for October", "October", "June"))
