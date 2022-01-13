# change global variable inside local scope

x = 100

def f():
    global x
    x += 1
    print(x)

f()

# if we don't use the keyword global, it will give error saying
# UnboundLocalError: local variable 'x' referenced before assignment
