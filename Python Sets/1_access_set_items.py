# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.
# Example
# Loop through the set, and print the values
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
# Example
# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
if "banana" in thisset:
    print("banana is in thisset")

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

tmp = list(thisset)
tmp.append("orange")
thisset = set(tmp)
print(thisset) # OUTPUT：{'cherry', 'orange', 'banana', 'apple'}
# Actually, sets can be added items by converting into a list
