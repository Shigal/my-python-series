# optional parameter
def f(y = 1):
    if y == 1:
        print(1)
    else:
        print("It is not 1")


# f() -----> gives 1
# f(2) -----> gives "It is not 1"



#--------------------------------------------------------------------


# required & optional
def required_optional(x, y=10):
    return x+y

# required_optional(5) -----> 15
#required_optional(5,11) ----> 16
