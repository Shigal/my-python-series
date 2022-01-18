# self is useful to define and access variables that belong to our Object
# for that we need to define a special method called __init__ (not _init_)
# init stands for initialize
# when we instantiate an object,if we defined a method __init__,
# python automatically calls the _init_method for you when the object is created
# inside _init_ we can give our Apple object variables 

class Apple:
    print('Apple created')

    def __init__(self):
        self.color = 'red'
        self.weight = 10

    def print_apple(self):
        print(self)
        print(self.color)
        print(self.weight)


apple = Apple()
apple.print_apple()


# Output:
# Apple created
# <__main__.Apple object at 0x000001DBDC4A5400>
# red
# 10
