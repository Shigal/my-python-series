# class variable vs instance variable
# instance variable - defined with syntax self
# instance variables are belong to the object that created them

class Vegetable:
    def __init__(self, name):
        self.name = name

veg = Vegetable('brinjal')
print(veg.name) # brinjal
