class Dog:
    name = None
    id = None

    def __init__(self):
        print("Default no Argument")

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def sleep(self):
        print("Sleeping")


dog1 = Dog("Chow", "1")
dog2 = Dog()
print(dog1.name)
print(dog1.id)