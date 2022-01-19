# class variable
# class variables belong to both the class that created them and the object
# access class variables with the class object Pyhton creates for each class
# here, we never created a Vegetable object, yet we were able to access the colors class variable
# as class variables can be accessed by the class that created them
# class variables can also be accessed by the object



class Car:
    colors = ['green', 'yellow', 'white', 'red']

    def __init__(self, name):
        self.name = name

print(Car.colors)
car = Car('Ferrari')
print(car.colors)

# Output:
# ['green', 'yellow', 'white', 'red']
# ['green', 'yellow', 'white', 'red']


