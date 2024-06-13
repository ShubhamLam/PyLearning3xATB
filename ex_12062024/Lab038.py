# Conditions
# age > 18 -> You are allowed to go to club
# age < 18 -> You are not allowed

# shubham -> goa -> Father permission
# shubham -> no goa -> no permission

# If, Else
# Syntax
# if condition:
#     code is executed
#     else:
#     code to be executed when condition is false

# Write a program to take a user age and let him know if he can go the club.

# Take a user input

age = int(input("Enter your Age\n"))

if age > 18:
    print("You are allowed to go to club")
else:
    print("You are not allowed")

