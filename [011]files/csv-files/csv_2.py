# read from a csv file
# reader method returns an iterable, we can iterate through to print each row
# call join method on a comma to add a comma in between each value to print the contents of the file like it appears in the file


import csv

with open('csv_file.csv', 'r') as csv_file:
    my_reader = csv.reader(csv_file, delimiter = ',')
    for row in my_reader:
        print(','.join(row))
