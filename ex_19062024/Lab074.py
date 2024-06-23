numbers = [1, 2, 3]


# collection of items

def do_something(pramod_list):
    pramod_list.append(100)
    pramod_list[0] = 123
    return pramod_list


def shanti():
    print("Shajnk")


l = do_something(numbers)
print(l)
shanti()
