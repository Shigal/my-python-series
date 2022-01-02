#Nested function

def x():
    
    print("Outer function")
    
    def y():
        
        print("Inner function")

    y()
x()
