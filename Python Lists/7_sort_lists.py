# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# Example:
# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# Example:
# Sort the list numerically:
thatlist = [1, 2, 3, 5, 612, 41, 77]
thatlist.sort()
print(thatlist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
# Example:
# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
# Example:
# Sort the list descending:
thatlist = [1, 2, 3, 5, 612, 41, 77]
thatlist.reverse()
print("thatlist.reverse()", thatlist)
thatlist_2 = [1, 2, 3, 5, 612, 41, 77]
thatlist_2.sort(reverse = True)
print("thatlist_2.sort(reverse = True)", thatlist_2)


# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# Example
# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:
# Example
# Perform a case-insensitive sort of the list:
thislist = ["Banana", "banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting oderder of the elements.
# Example
# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)