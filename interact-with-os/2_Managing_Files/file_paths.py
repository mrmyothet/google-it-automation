import os

# outputs["current_directory_before"] = os.getcwd()

cwd = os.getcwd()
print(cwd)

listdir = os.listdir()
print(listdir)

path_value = os.environ.get("PATH")
print(path_value)
