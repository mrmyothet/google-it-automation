name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name) * 3))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))


def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print("{:>3}F | {:>6.2f} C".format(x, to_celsius(x)))


def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
