import os
import datetime


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
        print(os.path.abspath(filename))
        filesize = os.path.getsize(os.path.abspath(filename))

    return filesize


print(create_python_script("program.py"))


def new_directory(directory, filename):
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    os.chdir(directory)
    with open(filename, "w") as file:
        pass

    os.chdir("..")
    return os.listdir(directory)


print(new_directory("PythonPrograms", "script.py"))


def file_date(filename):
    with open(filename, "w") as file:
        pass

    timestamp = os.path.getmtime(filename)
    date = datetime.datetime.fromtimestamp(timestamp)

    return "{}".format(str(date)[:10])


print(file_date("newfile.txt"))


def parent_directory():
    relative_parent = os.path.join(os.getcwd(), "..")

    return os.path.abspath(relative_parent)


print(parent_directory())
