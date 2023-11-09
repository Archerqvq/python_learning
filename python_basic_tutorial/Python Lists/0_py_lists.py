# List
# Lists are used to store multiple items in a single variable.

# List are one of FOUR bulit-in data types in Python used to store collections
# of data, the other THREE are Tuple, Set, and Dictionary, all with different
# qualities and usage.

# Lists are created using square brackets:
# Example:
# Crtea a list:
thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Items
# List items are orders, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has
# index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defiend order
# and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

# Note: There are some list methods that will change the order, but in general:
# the order of the items will not change.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a
# list after it has been created.

# Allow Duplicates
# Since lists are created, lists can have items with the same value:
# Example:
# List allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length
# To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List items - Data Types
# List items can be of any data type:
# Example
# String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3, 5, 6]
list3 = [True, False, True]
# A list can contain different data types:
# Example
# A list with strings, integers and boolean values:
list4 = ["abc", 34, True, 40, "male"]

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':
# <class 'list'>

# Example
# What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
# Example
# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry", "orange"))  # note the double round-brackets
print(thislist)

# The del keyword also removes the specified index:
# Example
# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)

# The del keyword can also delete the list completely.
# Example
# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
