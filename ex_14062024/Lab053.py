#Multipe conditions
# Switch in java
# Match case
numbers = int(input("Enter the number\n"))
browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed")
    case "firefox":
        print("FF code executed")
    case _:
        print("No browser found")

