# The error message just like below:
#
# Traceback (most recent call last):
#   File "<string>", line 6, in <module>
# ERROR!
# TypeError: MyClass.my_method() takes 0 positional arguments but 1 was given
#

# The error message "takes 0 positional arguments but 1 was given" typically occurs in Python when
# you define a method that does not take any argument except for self, but you attempt to call it with
# an extra argument.

class MyClass:
    def my_method():
        print("This method is supposed to take no arguments besides self.")


# Creating an instance of MyClass and trying to call my_method with an argument
my_instance = MyClass()
my_instance.my_method(1)  # This will raise an error

# ATTENTION:
# When you call my_instance.my_method(1),
# Python tries to pass the instance my_instance as the first argument, which is self, and 1 as the second argument.
# Since my_method is defined without any parameters other than the implicit self, it cannot accept the additional 1 argument,
# thus causing the error.
#
# To fix this error, you should either modify the method definition to accept the correct number of arguments or change the way you are calling the method to match the definition.
# If the method is not supposed to take any arguments other than self, you should call it without passing any extra arguments:

# Actually, it does not work, thx Chat-GPT : )
# This will raise an error too!!!!!!!!!!!!!!!!!!!!
my_instance.my_method()  # Correct way to call the method if no additional arguments are expected


# The right fixed solution should be like below
# If the method is supposed to take additional arguments, you should define it accordingly:
class MyClass_1:
    def my_method(self, value):
        print(f"This method takes one argument beside self: {value}")


# Now you can call it with oen argument
my_instance_1 = MyClass_1()
my_instance_1.my_method(1)


# -----------------------------------------------------------------------------------------------------------------
# Here is another example
# The code snippet you provided will actually result in an error because my_method() is defined without any parameters,
# including the self parameter that is expected for instance methods.
# Here is the corrected version of your MyClass definition with my_method correctly accepting self:
class MyClass_5:
    def my_method(self):  # Include 'self' to accept the instance reference
        print("This method is supposed to take no argument besides self.")


my_instance_2 = MyClass_5()
my_instance_2.my_method()  # This will work correctly now
# By including self as the first parameter in the definition of my_method, you are allowing it to be called on an instance
# of MyClass_5, which automatically passed the instance to the method as the first argument.
# The corrected code will not raise an error and will output.
