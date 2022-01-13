# Exception Handling: - for input from user could cause raise an exception

x = input("Enter your first number:")
y = input("Enter your second number:")
x = int(x)
y = int(y)

try:
    print(x/y)
except ZeroDivisionError:
    print("y cannot be zero. Please try again")

# If the user enters anything other than zero,code in try block gets executed and except block will not be executed
# If the user enters zero, instead of raising an exception, the code in except block gets executed
