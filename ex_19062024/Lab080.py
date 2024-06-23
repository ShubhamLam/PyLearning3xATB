# List
# List - Collection of Items (Duplicate is allowed)
my_list = [1,2,3]
my_list2 = [1, True, "Shubham", 12.34]

#Indexing
print("Element at Index 0:" , my_list[0])

#Changing an element
my_list[1] = 20
print("list after changing element index 1:", my_list)

#append()
my_list.append(4)
print("List after appending:", my_list)

# extend()
my_list.extend([5,6])
print("list after extending:", my_list)

#insert()
my_list.insert(1, "a")
print("List after inserting 'a' at index 1:", my_list)

# remove()
my_list.remove('a')
print("List after removing 'a':", my_list)

#copy()
my_copy_list = my_list.copy()
print(my_copy_list)

#clear()
my_list.clear()
print("Initial list:", my_list)
print(my_copy_list)

#print("Index of 3 in the list:", my_list.index(3))

#sort()
my_copy_list.sort()
print(my_copy_list)

#reverse()
my_copy_list.reverse()
print(my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])


