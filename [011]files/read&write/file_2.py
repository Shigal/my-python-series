# most preferred way to open a file in Python is to use a compound statement
# use with keyword
# using this, it automatically closes the file
# as long as we are inside with statement, we can work with the file we opened using the variable
# as soon as Python leaves with statement, it closes the file for us
# if we write something for the second time, what was written initially will be overwritten by new message

with open('my_file.txt', 'w') as my_file:
    my_file.write("Writing using \'with\' keyword")
