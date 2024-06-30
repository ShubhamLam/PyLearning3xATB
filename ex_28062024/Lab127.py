class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "Protected123"
        self.__private_var = "pass@123"


    def __private_method(self):
        print("Protected!")

    def printname(self):
        self.__private_method()
        if self.__private_var == "123":
            print("Hi , 123")
        print("I am allowed public")

#This is end of the class

alto = Car()
alto.printname()
# alto.__private_var
