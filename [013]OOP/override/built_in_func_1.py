# override built-in function

class Lion:
    def __init__(self, name):
        self.name = name


lion = Lion('Aslan')
print(lion) # <__main__.Lion object at 0x0000021B13071790>

# when we print our Lion object, python calls __repr__ method on our object
# which it has inherited from the Object parent class
# it prints whatever the __repr__method returns
# we override it

class Tiger:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

tiger = Tiger('Richard Parker')
print(tiger) # Richard Parker
