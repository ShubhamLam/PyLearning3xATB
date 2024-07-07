print("---Start the program---")
try:
    a = int(input("\nEnter the num1")) #ValueError: Invalid Error
    b = int(input("\nEnter the num2"))
    c = a / b #ZeroDivisionError
    print("Result Div is", c)
except Exception as e:
    print(e)
    print("Please enter Integer!")


print("---End of the Program---")

