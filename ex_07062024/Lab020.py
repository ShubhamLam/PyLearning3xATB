# In built Functions -
# Function -> Repeat a task - You can use a function.
# print(),input, type(), format(), max, min, id(), sum(), avg()

#Strings
name = "Amit" # 0 to 3
# 0,1,2,3
# A,m,i,t
print(name)
print(type(name))
print(id(name)) # id is memory address which value is stored 2246871225792
print(len(name)) # Length always start from 1
#Lengh of String (1)
name = name.upper()   # .upper() is used for coverting string into upper case (Capital letter)
print(name)
name = name.lower()  # .lower() is used for coverting string into lower case (small letter)
print(name)
a = name.count('A')
print(a)
#print(name[4]) # string  index out of range

# Python - Immutable - that can't be changed
name[0] = "P" # 'str' object does not support item assignment
#print(name[0])

