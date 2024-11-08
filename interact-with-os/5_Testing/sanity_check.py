def divide(a, b):
    assert b != 0, "cannot divide by zero"
    return a / b


result = divide(10, 2)
print(result)

result = divide(10, 0)
print(result)
