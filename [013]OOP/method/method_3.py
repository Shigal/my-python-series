# changing class definition, so the user can pass in their own variables when
# they create a new Apple object

class Apple:
    print('Apple created')

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight



apple = Apple('green',9)
print(apple.color)
print(apple.weight)
apple.weight = 8
print(apple.weight)


# Output:
# Apple created
# green
# 9
# 8
