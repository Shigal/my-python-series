# global scope
x = 10
y = 20
z = 30

print(x) #10
print(y) #20
print(z) #30



# local scope
def y():
    m = 1
    n = 2
    print(m)
    print(n)
y()

def f():
    a = 5
    b = 15
print(a) # NameError: name 'a' is not defined, and stopped
print(b)

