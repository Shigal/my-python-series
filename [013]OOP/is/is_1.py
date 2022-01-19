

class Person:
    def __init__(self):
        self.name = 'Bob'


bob = Person()
the_same_bob = bob
print(bob is the_same_bob) # True - cause' both variables point to the same Person object

another_bob = Person()
print(bob is another_bob) # False - cause' variables point to different Person objects
