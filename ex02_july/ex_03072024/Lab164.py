class Parent:
    def __init__(self):
        print("I am a parent")


class Son(Parent):
    def __init__(self):
        super().__init__()


s = Son()