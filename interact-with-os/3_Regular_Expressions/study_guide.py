import re

pattern = r"\d{3}-\d{3}-\d{4}"
us_phone_number = "111-222-3333"
print(re.search(pattern, us_phone_number))

pattern = r"^-?\d*(\.\d+)?$"
positve_number = "334"
negative_number = "-334"
print(re.search(pattern, positve_number))
print(re.search(pattern, negative_number))

pattern = r"^(.+)\/([^\/]+)\/"
path_and_file_name = "/home/myothet/repos/google-it-automation/interact-with-os/3_Regular_Expressions/study_guide.py"
path = "/home/myothet/repos/google-it-automation/interact-with-os/3_Regular_Expressions"
print(re.search(pattern, path_and_file_name))
print(re.search(pattern, path))
