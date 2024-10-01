import os

print(os.getcwd())

# os.mkdir("new_dir")
# os.chdir("new_dir")
# print(os.getcwd())


# os.mkdir("newer_dir")
# os.rmdir("newer_dir")

sample_data_dir = os.getcwd() + "/sample_data"
# sample_data_dir = os.chdir("sample_data")
list_dir = os.listdir(sample_data_dir)
print(list_dir)

os.chdir("..")
dir = "interact-with-os"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    # print(fullname)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
