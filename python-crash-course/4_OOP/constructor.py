class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self) -> str:
        return "an apple which is {} and {}".format(self.color, self.flavor)


honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")

print(honeycrisp.flavor)
print(fuji.flavor)

print(honeycrisp)

# Methods
# functions that operate on the attributes of a specific instance of a class


class Piglet:
    name = "piglet"
    years = 0

    def pig_years(self):
        return self.years * 18

    def speak(self):
        print("Oink! I'm {}! Oink".format(self.name))


hamlet = Piglet()
hamlet.speak()

hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

# Variables that have different values for different instances of the same class
# are called instance variables

piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())
