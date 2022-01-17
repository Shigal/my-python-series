# can only call read on a file once
# save the contents from the file, need a variable or container
# here, the program reads content as letters and save as characters inside a list

my_list = list()

with open("my_file.txt", "r") as my_file:
    for line in my_file.read():
        my_list.append(line)

print(my_list)
