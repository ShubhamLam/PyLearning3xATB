# Polymorphism
# Polymorphism allows objects of
# different classes to be treated as
# objects of a common superclass.

# The word "polymorphism" means "many forms",
# and in programming it refers to methods/functions/operators
# with the same name that can be executed on many objects or classes.

# Pramod -> Mentor, Husband, Brother.
# Object -Method -> Mother, Matenal She is, sister, parent -

# Method overriding

class Shape:
    def area(self):
        print("Area of the shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


Shape1 = Rectangle(3,4)
print(Shape1.area())

Shape2 = circle(10)
print(Shape2.area())

shape3 = Shape()
shape3.area()











