# open function creates a file object
# save our file object returned by the open function in a variable
# when we don't close the file, while runnung this module, we will get permission denied error


my_file = open('my_file.txt', 'w') 
str1 = "Hello World"
my_file.write(str1) # call write method on file object
my_file.close() # call close method on file object

