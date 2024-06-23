# Tuple - Collection of Items

my_list = [1, 2, 3, 4, 5]
print(id(my_list))
my_list[0] = 21 # Mutable -> we can change value in List
print(my_list)
print(id(my_list))

my_tuple = (1,2,3,4,5,5)
# my_tuple[0] = 21  # Immutable -> we cannot change value in tuple
print(my_tuple)