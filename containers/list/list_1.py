# Containers in Python
# lists

my_list1 = list (("apple", "orange", "pineapple", "guava"))
my_list2 = ["carrot", "beetroot", "potato", "yam"]
print(my_list1)
print(my_list2)


# append new item to the end of the list
my_list1.append("grapes")
my_list1.append("banana")
print(my_list1)

# we can store any datatype into a list
my_list1 = [2, True, 12.343, "hello"] # here true should start with capital T
print(my_list1)


# position of item - index of item
print(my_list1[0])

# change the item in the list by pointing the index of that item
months = ['January', 'February', 'March', 'May']
months[3] = 'April'
print(months)

# remove last item from the list
item = months.pop()
print(item)

# check if an item is in the list
week_list = ['Monday', 'Tuesday', 'Sunday']
x = 'Sunday' in week_list # capital small matters
print(x)

# get the size of the list
l = len(week_list)
print(l)

# slicing of list
months[0:3]
print(months)
