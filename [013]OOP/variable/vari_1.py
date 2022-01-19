# variable point to an object

# number points to an integer object with the value 100
number = 100

# when we assign a new value to number, it points to a new integer object with value 101
# old integer object with a value of 100 is discarded because it is no longer being used
number = 101


# two variables can point to the same object
# x points to an integer with a value of 100,
# when we assign y to x, y now points to the same integer object x points to
# x & y points to an integer object with a value of 100
x = 100
y = x
