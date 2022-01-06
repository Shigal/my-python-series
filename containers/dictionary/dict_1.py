# creating dictionaries
my_dict_1 = dict()
my_dict_2 = {}

my_dict_3 = {"Canada": "Ottawa", "India": "New Delhi", "Malaysia": "Kuala Lumbur"}
print(my_dict_3)

my_dict_4 = dict({"RCB": "Kohli", "CSK": "Dhoni", "RR": "Karthik"})
print(my_dict_4)

# using key to lookup a value
my_dict_3['India']

# adding more key value pairs
my_dict_5 = {"Microsoft": "USA"}
my_dict_5["Apple"] = "USA"
my_dict_5["Huawei"] = "China"
my_dict_5["SamSung"] = "South Korea"
print(my_dict_5)


# checking if a key is in a dictionary
print("Apple" in my_dict_5)

# deleting a key value from the dictionary using del keyword
del my_dict_5["Huawei"]
print(my_dict_5)
