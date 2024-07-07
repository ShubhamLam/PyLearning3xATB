#File IO
import os.path

try:
    file = open('example.txt', 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("I am not able to find the file. Please check path")
finally:
    print("Executed")
    try:
        file.close() #close has to be executed
    except NameError as ne:
        print(ne)
