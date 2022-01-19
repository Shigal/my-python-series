# x,y points to the same list
# we make a change to that single list object
# when we print both variables, it prints the list object they both point to 


x = [1,2,3]
y = x
y[2] = 100
print(x) # [1, 2, 100]
print(y) # [1, 2, 100]
