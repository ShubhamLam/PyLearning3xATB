class Person:
    #class  Variables / instance variables
    name = "Amit"
    age = None


    def walk(self):
        a = 10 # Local variable
        print("I am a Method")
        print("Hi", self.age)


amit = Person()
amit.walk()
