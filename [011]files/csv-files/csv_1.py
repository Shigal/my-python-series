# inside with statement we need csv module to convert our file object into a csv object
# csv module has a method: writer() which accepts file object and delimiter as parameters
# csv, writer method returns a csv object
# writerow method is used to write to our csv file
# writerow accepts a list as a parameter, each item is written to the csv file and separated by delimiter
# writerow only writes one row


import csv

with open('csv_file.csv', 'w') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ',')
    my_writer.writerow(['one', 'two', 'three'])
    my_writer.writerow(['four', 'five', 'six'])
