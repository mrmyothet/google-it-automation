class Triangle:
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __add__(self, other):
        return self.area() + other.area()


triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)

print("The area of triangle 1 is ", triangle1.area())
print("The area of triangle 2 is ", triangle2.area())
print("The area of both triangle is ", triangle1 + triangle2)

# https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
