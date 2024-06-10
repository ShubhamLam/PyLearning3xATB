# Strings
# Bunch of char
# '', "" , """
name = 'Harry'
print(name)
name = "Harry"
print(name)
name = """Harry, is a good person
He love to walk alone, He has a dog
 ....
 ...
 
 ...
 """
print(name)

# Raw String
dir = r'C:\nomedir\some dir'
print(dir)

#format of the String
first_name = "Harry"
last_name = "Potter"
print(first_name + " " + last_name)
print(first_name, last_name)

#f -> formatting - it will replace  the values of variables
#{} -> placeholders
print(f'your full name is {first_name} {last_name}')
print('your full name is', first_name, last_name)
