class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, balance):
        self.balance += balance

    def __withdraw(self, balance):
        self.balance -= balance

    def __show_balance(self):
        print("Your balance is", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_you_are_auth_users(self, auth, balance):
        if auth:
            self.__withdraw(balance=balance)
        else:
            print("Not Allowed")

jp_chase = BankAccount()
jp_chase.deposit(100)

secret_pass = input("Enter you pin to see balance")
if secret_pass == "1234":
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth(False)

secret_pass = input("Enter your PIN to Withdraw")
your_amount = int(input("Enter your amount to withdraw"))
if secret_pass == "1234":
    jp_chase.if_you_are_auth_users(True, balance=your_amount)
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth_users(False)

