class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")

class Child(Parent):

    def BHK3(self):
        print("3BHK")


child_object = Child()
child_object.BHK3()
child_object.BHK2()
print(child_object.gold)

parent_object = Parent()
parent_object.BHK2()
parent_object.gold
# parent_object.BHK3()

