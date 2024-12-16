# Debugging with assert


def read_file(file_name):

    assert file_name != "", "You must specify a file name!"

    with open(file_name, "r") as file:

        # Do something
        pass


read_file("")
