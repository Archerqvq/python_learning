# The f before the quotation marks in
#
# f"The property value is {self.my_property}"
#
# indicates that the string in an f-string, which stands for "formatted string literal."
# F-strings were introduced in Python 3.6 to provide a more convenient and readable way you
# include expressions inside string literals for formatting.

# Here's an example:

class MyClass:
    def __init__(self, value):
        self.my_property = value

    def my_method(self):
        return f"The property value is {self.my_property}"


my_instance = MyClass(123)
print(my_instance.my_method())  # Output: The property value is 123

# In the my_method method, the expression self.my_property inside the curly braces is replaced by its
# value when the method is called. In this case, if my_instance.my_property is 123, the output string
# will be "The property value is 123".
