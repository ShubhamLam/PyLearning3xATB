# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

Number = float (input("enter the first number\n"))
square = Number ** 2
cube = Number ** 3
print("square of number is", square )
print("Cube of number is", cube )

#Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

Num1 = int(input("Enter the first number\n"))
Num2 = int(input("Enter the second number\n"))

if Num1 > Num2:
    print(f"{Num1}  is greater than {Num2}")
elif Num1 < Num2:
    print(f"{Num1} is smaller than {Num2}")
else:
    print(f"{Num1} is equal to {Num2}")
