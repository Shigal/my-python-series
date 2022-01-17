# access the contents of a file
# call read method on our file object which returns an iterable
# using iteralbe we can iterate through to get each line of the file


with open('my_file.txt') as my_file:
    for line in my_file.read(): # print vertically
        print(line)


with open('my_file.txt') as my_file:
    for line in my_file.readline(): # print vertically
        print(line)



with open('my_file.txt') as my_file:
    for line in my_file.readlines(): # print horizontally the line
        print(line)
