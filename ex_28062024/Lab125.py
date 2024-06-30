# Web Automation - Selenium
# Page - You are going automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "Shubhamlambole@gmail.com" and self.password == "Shubham123":
            print("Allowed to enter")
        else:
            print("Not Allowed")

#This is end of the class

email = input("Enter your email")
password = input("Enter your password")
amit = VWOLoginPage(email, password)
amit.login_confirm()

email = input("Enter the email \n")
password = input("Enter the password \n")

pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
pramod.login_confirm()

