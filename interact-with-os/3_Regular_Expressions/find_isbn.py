import re


def find_isbn(list):
    pattern = r"(\d{3}-)(.*)-(\d{6})-(\d{1})"  # enter the regex pattern here
    result = re.search(pattern, list)  # enter the re method  here
    if result is None:
        return ""
    return result[3]  # return the correct capturing group


print(find_isbn("123-4-12-098754-0"))  # Should return 098754
print(find_isbn("223094-AB-30"))  # result should be blank
print(find_isbn("1123-4-12-098754-0"))  # result should be blank
