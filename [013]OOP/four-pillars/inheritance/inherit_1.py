# lbs - pounds
# by passing in Adult to our Kid class, Kid class inherits the variables and methods of Adult class
# not having to repeat code makes program smaller and more manageable
# create Kid class with all of the functionality of Adult class + additional functionality,
# all without affecting Adult class

class Adult():
    def __init__(self, name, height, weight, eye_color):
        """ height is in feet, weight in lbs """
        self.name = name
        self.height = height
        self.weight = weight
        self.eye_color = eye_color

    def print_name(self):
        print(self.name)

class Kid(Adult):
    def print_cartoon(self, fav_cartoon):
        print('{}\'s favourite cartoon is {}'.format(self.name, fav_cartoon))

child = Kid('John', 5, 45, 'green')
print(child.name)
print(child.height)
print(child.weight)
print(child.eye_color)

child.print_name()
child.print_cartoon('Horrid Henry')


# Output:
##John
##5
##45
##green
##John
##John's favourite cartoon is Horrid Henry
