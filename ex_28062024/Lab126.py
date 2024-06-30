# Encapsulation -
# bind the data values with the methods
# Data member -/ class Variables
# Methods - Def func within the class
# Wrapping or binding the data variables with the methods - Encapsulation.

# Hide the data members (class variables, instance variables) by using only the method

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when a object is created")

    def change_password(self):
        self.password = "345"
        print(self.password)


# THis is end of the class

xuv = Car()
xuv.password = "345"
xuv.change_password()
