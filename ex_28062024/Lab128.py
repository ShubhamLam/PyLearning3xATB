class Myclass:
    def __init__(self):
        self.name = "Amit"
        self.email = "amit@gmail.com"

    def public_func(self):
        print("Public func()")

    def __private_func(self):
        print("you can only access me via a another method, This is a private")

    def public_fn_private(self):
        self.__private_func()
        print(self.email)

# Security -> Not everyone can access your variables/methods, f(n)
a = Myclass()
a.public_func()
a.public_fn_private()
