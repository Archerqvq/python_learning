# Access Items
# List items are indexed and you can access them by referring to the index number:
# Just like using indexs to access specific character in strings, we have learned this before
# Example
# Print the seond item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Note: The first item has index 0.

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Example
# Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item:
# Example
# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# By leaving out the end value, the range will go on to the end of the list:
# Example
# This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])