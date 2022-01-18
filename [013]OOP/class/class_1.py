# define and create class in python
# the message given is printed as soon as we instantiate our Apple object
# type function tells that our Apple object is an instance of the Apple class we just created
# when we print our Apple object, python lets us know it is an Apple object, 
# and then gives us its location in the memory

class Apple:
    print("Apple is created")

apple = Apple()
print(type(apple))
print(apple)

# Output:
# Apple is created
# <class '__main__.Apple'>
# <__main__.Apple object at 0x000001832CAEE280>
