# In Python, self represents the instance of the class. By using the self keyword in a class
# you can access the attributes(variables) and methods(functions) of the class in Python.
# It binds the attributes with the given arguments.

# The reason you need to use self is to differentiate between instance attributes and local
# variables.

# When you create an instance of a class, Python passes the instance to the first parameter of
# the method, which by convention is called self.

# Here's how it works in the __init__ method:

# Here's how it works in the __init__ method:

class MyClass:
    def __init__(self, value):
        self.my_property = value  # self.my_property is an instance attribute


# When you create an instance of MyClass:

my_instance = MyClass(10)


# The instance my_instance is automatically passed to the __init__ method as the first parameter,
# which we refer to with self.

# Inside the method, self.my_property = value sets the my_property attribute of the my_instance
# object to 10.


# The use of self is consistent throughout class methods:

class MyClass_1:
    def __init__(self, value):
        self.my_property = value

    def my_method(self):
        # Use self to refer to the same object's attribute
        return self.my_property


# When my_instance.my_method() is called, Python again automatically passes my_instance to
# the my_method as the self parameter. This allows you to access the my_property attribute
# set earlier in __init__ method.


#### HOW ABOUT self? ####

# self is not a keyword in Python. It's a naming convention for the first parameter of instance
# methods in Python classes, which refers to the instance on which the method s being called.
# Python does not enforce the use of the name self; you could technically use any name you like
# for this parameter. However, it is a very strong convention, and not using self would likely
# confuse other programmers and is generally considered bad style.

# Here's an example that uses self by convention:

class MyClass_2:
    def __init__(self, value):
        self.my_property = value

    def my_method(self):
        return self.my_property


# And here's the same example using a non-standard name for the instance reference, which is
# not recommended:

class MyClass_3:
    def __init__(instance, value):
        instance.my_property = value

    def my_method(instance):
        return instance.my_property


instance = MyClass_3(10)

print(instance.my_method())


# While the second example will work correctly, it goes against the common practice and reduces
# the code's readability, so it's best to stick with self

# -----------------------------------------------------------------------
# The __init__ method is not strictly necessary for a class in Python, The __init__ method is a special
# method called a "constructor", which is called when an instance of the class is created.
# It's typically used to initialize attributes of the class.

# However, if your class does not need any initialzation, you can omit the __init__ method, and Python will
# create a default __init__ method for you that does nothing:

class MyClass_4:
    def some_method(self):
        return "Hello, World!"

    def other_method(self):
        return "How is your day?"


# You can still create an instance of MyClass_4
my_instance = MyClass_4()

# And call its methods
print(my_instance.some_method())  # Output: Hello, World!
print(my_instance.other_method())
