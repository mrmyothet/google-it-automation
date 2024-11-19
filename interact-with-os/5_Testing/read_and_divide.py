# FileNotFoundError
# IndexError
# ValueError
# ZeroDivisionError


def faulty_read_and_divide(filename):
    with open(filename, "r") as file:
        data = file.readlines()
        num1 = int(data[0])
        num2 = int(data[1])
        return num1 / num2


# File-level issues
# ValueError: Not enough data in the file
# Error: The file was not found

# Data-level issues
# ValueError: invalid literal for int() with base 10: 'apple'
# DivisionError: The denominator is zero


def enhanced_read_and_divide(filename):
    try:
        with open(filename, "r") as file:
            data = file.readlines()

        if len(data) < 2:
            raise ValueError("Not enough data in the file")

        num1 = int(data[0])
        num2 = int(data[1])

        if num2 == 0:
            raise ZeroDivisionError("The denominator is zero.")

        return num1 / num2
    except FileNotFoundError:
        return "Error: the file was not found."
    except ValueError as ve:
        return f"Value error: {ve}"
    except ZeroDivisionError as zde:
        return f"Division error: {zde}"


# faulty_read_and_divide("numbers_file")
result = enhanced_read_and_divide("numbers_file")
print(result)
