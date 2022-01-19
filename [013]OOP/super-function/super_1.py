# use keyword super to call Mammal parent class's sleep method
# able to give a child class the functionality from a parent class's method
# without having to retype the functionality in the child class
class Mammal:
    def __init__(self, name):
        self.hunger = 100
        self.tired = 100
        self.name = name

    def print_result(self, amount, action):
        print("{}{} decreased by {}".format(self.name, action, amount))

    def sleep(self, decrease):
        self.tired = decrease
        self.print_result(decrease, 'tiredness')

class Tiger(Mammal):
    def sleep(self, decrease):
        # super.sleep(decrease) -----> AttributeError: type object 'super' has no attribute 'sleep'
        super().sleep(decrease)
        print("Tiger is really tired")


tiger = Tiger('tiger')
tiger.sleep(10)


# Output:
# tigertiredness decreased by 10
# Tiger is really tired
