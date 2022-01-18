# when we think of what our object Apple can do


class Apple:
    def __init__(self):
        """ all weights are in oz """
        self.weight = 10
        self.color = 'red'
        self.mold = 0

    def rot(self, days, temperature):
        self.mold = days*(temperature*.1)

apple = Apple()
print(apple.mold)
apple.rot(10, 99)
print(apple.mold)


# Output:
# 0
# 99.0
