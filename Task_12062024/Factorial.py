# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

num = int(input("Enter the number:"))

i = 1
fac = 1

while i <= num:
    fac = i * fac
    i = i + 1


print(fac)


# 1*1 =1
# 2*1 =2
# 3*2 =6
# 4*6 =24
# 5*24=120