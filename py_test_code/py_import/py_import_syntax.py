# In python, you can import classes from other modules in several ways,
# each serving different need in terms of namespace management and code
# organization. Here are the most common methods.

# 1.
# Import an entire module: This brings the entire module into your
# namespace. You would then access the class using the module name as
# a prefix.

import math  # import module_name

instance = math.sqrt(3)  # instance = module_name.ClassName()

# 2.
# Import a specific class from a module: This imports only the
# specific class from the module. The class can be used without
# module prefix.

from math import sqrt  # from module_name import ClassName

instance = sqrt(3)  # instance = ClassName()

# 3.
# import multiple classes from a module: Similar to the above method,
# but for multiple classes.

from math import sqrt, sin  # from module_name import ClassName1, ClassName2

instance1 = sqrt(3)  # instance1 = ClassName1()
instance2 = sin(5)  # instance2 = ClassName2()

# 4.
# Import all classes and definitions from a module: While convenient,
# this is generally discouraged as it can lead to namespace pollution
# and make it harder to indentify where a class came from

from math import *  # from module_name import *

instance = sqrt(3)  # instance = ClassName()
# Assuming ClassName is defined in module_name

# 5.
# Import a module with an alias: This is useful when module names
# are long or when you want to avoid a namespace collision.

import math as m  # import module_name as alias

instance = m.sqrt(3)  # instance = alias.ClassName()

# 6.
# Import a class with an alias: This is similar to importing a class
# directly, but you give it a different name in your namespace.


from math import sqrt as sq  # from module_name import ClassName as Alias

instance = sqrt(3)  # instance = Alias()


# 7.
# Import a module or class within a function or local scope: This is less
# common but can be used to reduce the scope of an import to a function.

def function():
    from math import sqrt  # from module_name import sqrt
    instance = sqrt(5)  # instance = ClassName()
    # Do something with instance
