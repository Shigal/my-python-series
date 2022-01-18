# By defining a method and print self, we can see it is the Apple object
# we called our method on
# self is useful to define and access variables that belong to our Apple object

class Apple:
    print("Apple created")

    def print_apple(self):
        print(self)

Apple().print_apple()


# Output:
# Apple created
# <__main__.Apple object at 0x000002877FF15430>
