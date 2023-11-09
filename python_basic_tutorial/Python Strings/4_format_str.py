# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# Example
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# ATTENTION:
#   File "D:\git\python_learning\Python Strings\4_format_str.py", line 5, in <module>
#     txt = "My name is John, I am " + age
#           ~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str
# Because we can not combine strings and numbers together !!!!

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them,
# and places them in the string where the placeholders {} are:
# Example
# Use the format() method to insert numbers into strings:
age = 35
txt = "My name is John, and I am {}"
print(txt.format(age))
combined_txt = txt.format(age)
print(combined_txt)

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
myorder_1 = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))
print(myorder_1.format(quantity, itemno, price))
