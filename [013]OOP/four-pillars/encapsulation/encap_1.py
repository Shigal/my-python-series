# get_data() method has a variable called data
# there is no way for user to access this variable because of encapsulation

class Data:
    def get_data(self, n):
        data = [1, 2, 3, 4, 5]
        data.append(n)


dat = Data()
dat.get_data(6)
print(dat)
