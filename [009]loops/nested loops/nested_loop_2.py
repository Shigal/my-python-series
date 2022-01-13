# add two lists into one

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7]

my_list = []

for i in list1:
    for j in list2:
        my_list.append(i+j)

print(my_list)


# Output: [3, 5, 7, 9, 5, 7, 9, 11, 7, 9, 11, 13, 9, 11, 13, 15]
