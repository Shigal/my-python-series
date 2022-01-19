# overriding methods
# when a class inherits a method from a parent, we have the ability to override it


class Mammal:
    def __init__(self, name):
        self.hunger = 100
        self.tired = 100
        self.name = name

    def print_result(self, amount, action):
        print('{} {} decreased by {}'.format(self.name, action, amount))

    def eat(self, decrease):
        self.hunger = decrease
        # print_result(decrease, 'hunger')-------> NameError: name 'print_result' is not defined
        self.print_result(decrease, 'hunger')

    def sleep(self, decrease):
        self.tired = decrease
        self.print_result(decrease, 'tiredness')

# Dolphin inherits all of its functionality from Mammal parent class without making any changes
class Dolphin(Mammal):
    pass

# Tigher defines a method called sleep, with different functionality than the
# sleep method it inherits from its parent class
class Tiger(Mammal):
    def sleep(self, decrease):
        self.tired = decrease
        print('The tiger is really tired')


dolphin = Dolphin('dolphin')
dolphin.eat(10)
dolphin.sleep(10)

tiger = Tiger('tiger')
tiger.eat(10)
tiger.sleep(10)# new method we defined gets called instead of the inherited method


# Output:
##dolphin hunger decreased by 10
##dolphin tiredness decreased by 10
##tiger hunger decreased by 10
##The tiger is really tired



