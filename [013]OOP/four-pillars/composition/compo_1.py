# composition is used to represent 'has a' relationship
# eg:- dog has an owner

class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person():
    def __init__(self, name):
        self.name = name


# create dog object and pass in person object as owner parameter

jack = Person('Jack Sparrow')
dog = Dog('Bruno', 'German dog', jack)

print(dog.breed) # German dog
print(dog.owner) # <__main__.Person object at 0x00000211B72C3430>
print(dog.owner.name) # Jack Sparrow
