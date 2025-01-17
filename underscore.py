# In programming, especially in Python, "underscore" (_ or __) has several important uses:
#Single Underscore (_):

"""Temporary Variables: Commonly used to indicate that a variable is temporary or insignificant."""

for _ in range(5):
    print("Hello")

"""Interactive Interpreter: In Python’s interactive shell, _ is used to hold the result of the last executed expression."""

# >>> 5 + 3
8
# >>> _ * 2
16

# Special Use of Underscore in Numeric Literals
"""Underscores can be used in numeric literals to improve readability."""

large_number = 1_000_000
hex_number = 0x_1A_2B_3C
print(large_number)  # Outputs: 1000000
print(hex_number)    # Outputs: 1715004

# Unpacking Values with Underscore
"""Ignoring Values: Often used in unpacking when you want to ignore certain values."""
a, _, b = (1, 2, 3)
a, *_, b = (1, 2, 4, 7, 3)
print(a)  # Outputs: 1
print(b)  # Outputs: 3
print(_)  # Outputs: [2, 4, 7]

# Ignoring Values: Used when a value needs to be passed but is not going to be used.

def my_function(_, a, b):
    return a + b

print(my_function(10, 5, 3))  # Outputs: 8 (10 is ignored)

# Single Leading Underscore (_variable):

"""Weak "Internal Use" Indicator: A convention to indicate that a variable or method is intended for internal use. It is a hint for programmers and does not enforce any access restriction."""

class MyClass:
    def __init__(self):
        self._internal_var = 10  # Internal Variable

    def _internal_method(self):
        print("This is an internal method.")  # Internal Method

# Example:

class MyClass:
    def __init__(self):
        self._internal_var = 42  # Intended for internal use
        self.public_var = 100     # Can be accessed from outside

    def _internal_method(self):
        # Internal method, not meant to be called from outside
        print("This is an internal method.")

    def public_method(self):
        # Public method
        self._internal_method()
        print("This is a public method.")


obj = MyClass()
print(obj.public_var)       # Outputs: 100
print(obj._internal_var)    # Outputs: 42 (but is intended for internal use)

obj.public_method()         # Works fine
obj._internal_method()      # Works, but not recommended

# Single Trailing Underscore (variable_):

"""Avoiding Naming Conflicts: Used to avoid naming conflicts with Python keywords or built-in names."""

def function_(self):
    pass

# Double Leading Underscore (__variable):

"""Name Mangling: Triggers name mangling where the interpreter changes the name of the variable to include the class name. This is used to avoid conflicts in subclasses."""

""""Name Mangling" refers to the process by which the Python interpreter changes the name of a variable or method to include the class name, helping to avoid naming conflicts in subclasses. When you use double underscores (__) at the beginning of a variable or method name, Python automatically modifies its name to include the class name. This prevents naming conflicts in subclasses."""

class BaseClass:
    def __init__(self):
        self.__private_var = 42


class SubClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.__private_var = 100


base = BaseClass()
sub = SubClass()

"""
In BaseClass, the variable __private_var is defined. Python changes its name to _BaseClass__private_var.

In SubClass, another variable named __private_var is defined. Python changes its name to _SubClass__private_var."""

print(base._BaseClass__private_var)  # Outputs: 42
print(sub._SubClass__private_var)    # Outputs: 100


# Double Leading and Trailing Underscore (variable):

"""Magic Methods: Reserved for special use in the language. These methods have specific meanings and are used to implement certain behaviors in Python (e.g., __init__, __call__, __str__, etc.)."""

"""Magic Methods in Python, also known as dunder (double underscore) methods, are special methods that start and end with double underscores (__). These methods have special meanings and allow you to define or customize the behavior of your objects in Python. Here are some common magic methods and their uses:"""

"""magic methods are specifically designed for objects in Python. These methods allow you to define or customize the behavior of instances of your classes when they interact with built-in Python functions and operators. Here are some key points to understand:

Object-Oriented: Magic methods are integral to Python's object-oriented programming. They allow you to define how your objects behave in various situations.

Class Instances: Magic methods are defined within classes and are called on instances of those classes (objects).

Customization: They help customize behaviors like initialization (__init__), string representation (__str__), calling the object as a function (__call__), indexing (__getitem__), and more."""

class MyClass:
    def __init__(self):
        self.var = 10

    def __str__(self):
        return f"MyClass with var = {self.var}"

# Example

class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value {self.value}"

    def __call__(self, x):
        return x * self.value

"""Creating an instance of MyClass (an object)"""

obj = MyClass(10)

print(obj)            # Calls __str__, Outputs: MyClass with value 10
print(obj(5))         # Calls __call__, Outputs: 50

# Example

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Using the __add__ Method
print(v3)     # Output: Vector(6, 8)

# Instance Variables vs. Class Variables with Underscores
"""While it's more of a convention and not enforced by Python, using underscores can help indicate the intended scope and use of variables, making the code more readable and maintainable. Here’s how it works:"""

"""Instance Variables: Typically defined in methods like __init__, prefixed with a single underscore to indicate they are intended for internal use within instances"""

class MyClass:
    def __init__(self, value):
        self._instance_var = value

"""Class Variables: Often prefixed with a single or double underscore to prevent name clashes or to follow a naming convention, especially when they should not be accessed or modified directly."""

class MyClass:
    __class_var = 42  # Double underscore for name mangling and internal use


# Leading Underscore in Module Names
"""Internal Modules: A single leading underscore in module names indicates that the module is intended for internal use."""

# _internal_module.py

"""In Python, using a single leading underscore to indicate internal use is a hint to other developers that the module or variable is intended to be private and not accessed directly. It doesn't enforce access restrictions, meaning that technically, you can still access it if you know its name.

For example, you can still directly import and use _internal_module even if it's intended for internal use:"""

# This will work, but it's against the convention

from mypackage import _internal_module
_internal_module.internal_function()