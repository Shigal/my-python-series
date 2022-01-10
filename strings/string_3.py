# split method

my_string = "Live as if you were going to die tomorrow. Learn as if you were going to live forever"
print(my_string.split('.'))
# ['Live as if you were going to die tomorrow', ' Learn as if you were going to live forever']


#---------------------------------------------------------------------


# join method
my_str = "xyz"
my_result = '+'.join(my_str)
print(my_result)

my_list = ["the", "fox", "jumped", "over", "the", "fence"]
my_line = " ".join(my_list)
print(my_line)


#--------------------------------------------------------------------


# replace method
my_string = "The cat jumped over the hat."
my_result = my_string.replace('a', '@')
print(my_result)


#--------------------------------------------------------------------


# index method
my_string = "cat"
print(my_string.index('a'))


#-------------------------------------------------------------------

# in keyword
my_line = "A picture in the play magazine is most widely used in image processing"
print("picture" in my_line)

my_line = "A picture in the play magazine is most widely used in image processing"
print("computer" not in my_line)


#-------------------------------------------------------------------

# escapeing string
print("Hello, do you know \"Java\"?")

# new line
print("Hello \nhow are you?")

# concatenation
print("con"+"cate"+"nation")

# string multiplication
print("me" * 3)
