# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Example
# Get the value of the "model" key:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:
# Example
# Get the value of the "model" key:
x = thisdict.get("model")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
# Example
# Get a list of the keys:
x = thisdict.keys()
print(x)
# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
