# OS Module
# OS module use to interact with the operating system
# get working dir, change dir, file exist, file name, size file, Envir

import os
import math

print(os.name)   #nt - windows , posix for Linux -> Mac

# print(os.getcwd())
# print(math.pi)
#
# os.chdir("C:\\Users\\HP\\PycharmProjects\\Py3xLearning\\ex02_july")
# print(os.getcwd())

print(os.listdir("C:\\Users\\HP\\PycharmProjects\\Py3xLearning\\ex02_july"))

# os.mkdir("Shubham")


#Read file, you want to check if exist or not
size = os.path.getsize('testdata.txt')
print(size)

if size != 0:
    print("File exist and has content")
else:
    print("file not exist, NO content ")

#Get file modification time
mtime = os.path.getmtime('testdata.txt')
print(mtime)

import time
print(time.gmtime(mtime))
print(time.localtime())