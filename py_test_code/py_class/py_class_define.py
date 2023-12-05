# How to define a class in Python, Here are some examples

# To define a class inPython, you use the class keyword followed by
# the class name and a colon. Class names typically follow the CapWords
# convention. Inside the class, you can define methods(functions) and
# properties（variables).

# Here's an example of a simple Python class with an initializer method,
# one property, and one method.

class MyClass:
    # The initializer method, would be called when a new instance is created
    def __init__(self, value):
        self.my_property = value  # An instance property

    def my_method(self):  # A method
        return f"The property value is {self.my_property}"


# To create an instance of the class, you would call as if it were a function,
# passing the necessary arguments to the initializer method __init__, if any:

my_instance = MyClass(10)

# Now, my_instance is an object of MyClass, with my_property set to 10.
# You can call its method like this:

print(my_instance.my_method())  # Output will be "The property value is 10"


# Classes can also have variables(shared across all instances), static
# methods(callable without an instance), and class methods(callable without
# an instance but with access to the class object).

# Here's how you can add a clas variable and a static method:
class MyClass_1:
    class_variable = "I am a class variable"  # Class variable

    def __init__(self, value):
        self.my_property = value

    def my_method(self):
        return f"The property value is {self.my_property}"

    @staticmethod
    def my_static_method():  # Static method
        return "I do not need an instance to be called."


# Access the class variable
print(MyClass_1.class_variable)

# Call the static method
print(MyClass_1.my_static_method())



