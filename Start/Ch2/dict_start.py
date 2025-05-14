# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
myDict = {
    "name": "Joe",
    "age": 35,
    "city": "San Francisco",
    "state": "CA",
    "zip": 94105
}
print(mydict)
# Dictionaries are mutable, so you can change them
myDict["age"] = 36
# dictionaries are accessed via keys
print(myDict["name"])
# You can also use the get() method to access a value
print(myDict.get("age"))


# you can also set dictionary data by creating a new key
myDict["email"] = "test@example.com"
print(myDict)

# Trying to access a nonexistent key will produce an error
# print(myDict["email2"])
# To avoid this, you can use the get() method to return a default value
print(myDict.get("email2", "not found"))

# To avoid this, you can use the "in" operator to see if a key exists
print("email" in myDict)  # True
print("email2" in myDict)  # False

# You can retrieve all of the keys and values from a dictionary
print(myDict.keys())  # returns a list of keys
print(myDict.values())  # returns a list of values

# You can also iterate over all the items in a dictionary
for key, value in myDict.items():
    print(key, ":", value)

# You can also use the del statement to remove a key-value pair
del myDict["email"]
print(myDict)

# You can also use the pop() method to remove a key-value pair
myDict.pop("email2", "not found")  # returns the value or default