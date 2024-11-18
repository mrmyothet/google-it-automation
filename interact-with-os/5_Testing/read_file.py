import os


def is_locked(filename):
    lockFile = filename + ".lckchk"
    if os.path.exists(lockFile):
        return True
    return False


def is_not_accessible(filename):
    if not os.access(filename, os.R_OK):
        return True
    return False


def read_file(filename):
    if not os.path.exists(filename):
        print(filename, "does not exists.")
        return None
    if not os.path.isfile(filename):
        print(filename, "is not the file type.")
        return None
    if not os.access(filename, os.R_OK):
        print("cannot access ", filename)
        return None
    if is_locked(filename):
        print(filename, "is locked")
        return None
    if is_not_accessible(filename):
        print(filename, "is not accessible")
        return None

    f = open(filename)
    contents = f.read()
    return contents


def read_file_try(filename):
    try:
        f = open(filename)
        return f.read()
    except OSError:
        print("the system could not read ", filename)
        return None


contents = read_file("logfile")
print(contents)

contents = read_file_try("logfile.log")
print(contents)
