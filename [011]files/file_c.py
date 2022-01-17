name = input("Name: ")
age = input("Age: ")

with open('my_challenge.txt', 'w') as my_file:
    my_file.write(name+ ":" + age)
