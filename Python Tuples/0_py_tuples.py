mytuple = ("apple", "banana", "cherry")

# Tuple
# Tuples are used to store multiple items in a single variable

# Tuple is one of FOUR built-in types in Python used to store collections of data,
# the other THREE are List, Set and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

# Example
# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
# Example
# Tuples allow duplicate values:
thistuple = ("apple", "apple", "banana", "cherry", "cherry")
print(thistuple)

# Tuple Length
# To determine how many items a tuple has, use the len() function:
# Example
# Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item
# ATTENTION: #####################################
# To create a tuple with only one item,
# you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.
# ##################################################
# Example
# One item tuple, remember the comma:
thistuple = ("apple",)  # OUTPUT: <class 'tuple'>
print(type(thistuple))

# If tuple only has one item and without a comma after the item,
# the interpreter will recognize it as type of STR rather than TUPLE
# NOT A TUPLE
thistuple = ("apple")  # OUTPUT: <class 'str'>
print(type(thistuple))

# Tuple Items - Data Types
# Tuple items can be of any data type:
# Example
# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 2, 3, 4, 5)
tuple3 = (True, False, True)
# A tuple can contain different data types:
# Example
# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple':
# <class 'tuple'>
# Example
# What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# Example
# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# ATTENTION: IMPORTANT CONCEPTS
########################################################################################
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning, and,
# it could mean an increase in efficiency or security.
#########################################################################################
