# Multilevel Inheritance

class Grandfather:
    key_gold = "1 kg"
    def grandfather_mothod(self):
        return "Grandfather's method"

class Parent(Grandfather):
    def parent_method(self):
        return "Parent's method"

class Child(Parent):
    mac_m3_apple = "M3 Max"
    def child_method(self):
        return "Child's method"


child = Child()
print(child.grandfather_mothod())
print(child.parent_method())
print(child.child_method())
print(child.key_gold)
print(child.mac_m3_apple)

parent = Parent()
print(parent.parent_method())
print(parent.grandfather_mothod())
print(parent.key_gold)


grandparent_ref = Grandfather()
grandparent_ref.grandfather_mothod()
grandparent_ref.key_gold
