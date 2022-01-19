# x points to the integer object with the value 10,
# when we create y, it points to the same integer object
# when we increment x, x points to the new integer object with the value of 11
# but the integer object with the value of 10 is not discarded, becasue it is being used
# y still points to the integer object with value 10

x = 10
y = x
x += 1
print(x) # 11
print(y) # 10
