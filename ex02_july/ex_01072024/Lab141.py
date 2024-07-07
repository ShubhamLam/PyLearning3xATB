def multiple_return_one():
    return 99, "Promod", True

print(multiple_return_one())    # will print in the form of tuple by default
print(list(multiple_return_one()))
print(set(multiple_return_one()))