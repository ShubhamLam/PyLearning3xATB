# Inheritance
# Acquire the Attributes and Behaviour
# Data members and Methods

# 3BHK House -F -> Inheritance - Son -
# concept in object-oriented programming (OOP)
# that allows a class (child class) to inherit attributes and methods
# from another class (parent class)

# Types of Inheritance

# Single - 80%  - # API, Web Automation - 80% -> Single
# Multiple
# Multi level
# Hybrid
# Hierarchical


# Single
class Grandfather: #Parent class #Base class
    key = "abc@123"
    def grandfather_method(self):
        return "Grandfather's method"

class Father(Grandfather):   # Child Class, Sub Class
    def parent_method(self):
        return "Parent's method"


grandfather = Grandfather()
grandfather.grandfather_method()
# grandfather.father_method()

parent = Father()
print(parent.parent_method())

print(parent.grandfather_method())  # how parent is able to call the graparent? inheritance
print(parent.key)