class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def show_balance(self):
        print("Your balance is", self.balance)


jp_Chase = BankAccount()
print(jp_Chase.balance)
jp_Chase.deposit(101)
jp_Chase.show_balance()
jp_Chase.deposit(99)
jp_Chase.show_balance()
jp_Chase.withdraw(199)
jp_Chase.show_balance()
