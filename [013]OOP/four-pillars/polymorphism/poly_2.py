# create a function that can take any object, allowing for polymorphism
# any instantiated object will be able to be called into this function
# we can call the actions of classes Canada and Malaysia using this same func

class Canada:
    def capital(self):
        print('Capital of Canada is Ottawa')

    def language(self):
        print('A multitude of languages are used by Canadians such as English, French and etc')

    def type(self):
        print('Canada is a country in North America')
        
class Malaysia:
    def capital(self):
        print('Capital of Malaysia is Kuala Lumbur')

    def language(self):
        print('Official language and national language is Malaysian')

    def type(self):
        print('Malaysia is a southeast asian country')


""" implementing polymorphism with a function """
def func(obj):
    obj.capital()
    obj.language()


can = Canada()
malay = Malaysia()

func(can)
func(malay)


        
