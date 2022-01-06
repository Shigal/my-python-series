# create a tuple
my_tuple = tuple()
my_tuple = ()


# add items when creating a tuple
my_tuple = tuple(('cake', 'ice-cream', 'tart'))
print(my_tuple)
my_tuple = ("Ferrari", "Mercedes", "Sedan")
print(my_tuple)

# access an item from the tuple
print(my_tuple[0])

# slice the tuple
my_tuple[1:1]
print(my_tuple)

print("Mercedes" in my_tuple) # true, since no items can be removed from tuple
print("VW" not in my_tuple)


# using tuple ensures that other part of the program don't have the ability to accidently change it
