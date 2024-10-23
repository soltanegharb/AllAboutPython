# Tuples in Python
"""Tuples are a type of sequence in Python, similar to lists, but with a key difference: they are immutable, meaning their values cannot be changed once they are created."""
# Advantages of Tuples
"""
Immutability: Ensures data integrity.

Performance: Tuples are generally faster than lists.

Memory: Tuples use less memory."""

# Creating a Tuple
"""A tuple is created by placing all the items (elements) inside parentheses (), separated by commas:"""

my_tuple = (1, 2, 3)

# Accessing Elements
"""You can access elements in a tuple by using indexing:"""

print(my_tuple[0])  # Output: 1

# Creating a Singleton Tuple
"""To create a tuple with only one element, you need to include a comma:"""

single_element_tuple = (1,)

"""The reason for including a comma when creating a singleton tuple is to differentiate it from a regular expression enclosed in parentheses. Without the comma, Python interprets it as a simple value enclosed in parentheses rather than a tuple."""

"""Without the comma:"""
single_element = (5)
print(type(single_element))  # Output: <class 'int'>

"""In this case, single_element is treated as an integer."""

"""With the comma:"""
single_element_tuple = (5,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

# Immutability
"""Because tuples are immutable, you cannot change their values:"""
my_tuple = (1, 2, 3)
my_tuple[0] = 4  # This will raise an error

# Common Uses
"""Returning Multiple Values from a Function: Functions can return multiple values as a tuple."""

def get_coordinates():
    return (10, 20)


x, y = get_coordinates()
print(x, y)  # Output: 10 20

"""Functions can return multiple values as a tuple, which can then be unpacked:"""

def get_min_max(data):
    return min(data), max(data)


min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print(min_val)  # Outputs: 1
print(max_val)  # Outputs: 5

"""Storing Constants: Useful for storing multiple values that shouldn’t change."""
"""Dictionary Keys: Tuples can be used as keys in dictionaries (because they are immutable)."""

# Examples
"""Combining Tuples:"""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repeating Tuples:
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

# Tuple Packing and Unpacking
"""Packing: You can pack multiple values into a single tuple:"""

packed_tuple = 1, 2, 3
print(packed_tuple)  # Outputs: (1, 2, 3)

# Unpacking Tuples
"""You can unpack tuples into individual variables very conveniently:"""

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Outputs: 1
print(b)  # Outputs: 2
print(c)  # Outputs: 3

# Tuple Unpacking with Nested Structures
"""You can unpack nested tuples by mirroring the structure:"""

nested_tuple = (1, (2, 3), 4)
a, (b, c), d = nested_tuple
print(a)  # Outputs: 1
print(b)  # Outputs: 2
print(c)  # Outputs: 3
print(d)  # Outputs: 4

# Using Tuples as Dictionary Keys
"""Since tuples are immutable, they can be used as keys in dictionaries:"""

coordinates = {}
coordinates[(0, 0)] = "Origin"
coordinates[(1, 2)] = "Point A"
print(coordinates)  # Outputs: {(0, 0): 'Origin', (1, 2): 'Point A'}

# Nested Tuples
"""Tuples can contain other tuples, allowing you to create nested structures:"""

nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple[1][1])  # Outputs: 3

# Converting Between Lists and Tuples
"""You can easily convert lists to tuples and vice versa:"""

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Outputs: (1, 2, 3)

new_list = list(my_tuple)
print(new_list)  # Outputs: [1, 2, 3]

# Slicing Tuples
"""Similar to lists, you can slice tuples to get sub-tuples:"""

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Outputs: (2, 3, 4)

# Tuple Methods
"""count: Counts the occurrences of a value."""

my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Outputs: 3

"""index: Returns the index of the first occurrence of a value."""

my_tuple = (1, 2, 3, 2)
print(my_tuple.index(2))  # Outputs: 1

# Swapping Variables
"""One of the elegant uses of tuples is swapping the values of variables without needing a temporary variable:"""

"""the statement a, b = b, a uses tuples. What happens is that a temporary tuple (b, a) is created, and then this temporary tuple is used to swap the values of a and b"""
a = 10
b = 20
a, b = b, a
print(a)  # Outputs: 20
print(b)  # Outputs: 10

# Using Tuples in a for Loop
"""Tuples can be used directly in for loops to unpack each element:"""

points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"Point: x={x}, y={y}")
# Outputs:
# Point: x=1, y=2
# Point: x=3, y=4
# Point: x=5, y=6

# Default Arguments with Tuples
"""Tuples can be used to provide default arguments in functions:"""

def print_coordinates(coords=(0, 0)):
    print(f"X: {coords[0]}, Y: {coords[1]}")

print_coordinates((10, 20))  # Outputs: X: 10, Y: 20
print_coordinates()  # Outputs: X: 0, Y: 0

# Real-World Example
"""Let’s implement a simple function that calculates the area and perimeter of a rectangle and returns them as a tuple:"""


def rectangle_properties(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


area, perimeter = rectangle_properties(5, 10)
print(f"Area: {area}, Perimeter: {perimeter}")
# Outputs: Area: 50, Perimeter: 30

# Zipping and Unzipping Using Tuples
"""You can use zip to combine multiple lists into tuples, and then zip(*...) to unzip them:"""

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)  # Outputs: [(1, 'a'), (2, 'b'), (3, 'c')]

unzipped = zip(*zipped)
list1_unzipped, list2_unzipped = list(unzipped)
print(list1_unzipped)  # Outputs: [1, 2, 3]
print(list2_unzipped)  # Outputs: ['a', 'b', 'c']

# Named Tuples
"""Named tuples provide a way to access tuple elements by name, making your code more readable:"""
"""Namedtuples Explained
namedtuple is a factory function for creating tuple subclasses with named fields. It is part of the collections module. Namedtuples are similar to regular tuples, but the difference is that fields can be accessed by name instead of by index, making the code more readable and self-documenting.

Why Use Namedtuples?
Readability: Accessing elements by name improves code readability.

Immutability: Like regular tuples, namedtuples are immutable.

Memory Efficiency: Namedtuples are more memory-efficient than dictionaries."""

from collections import namedtuple

"""Define a named tuple type called 'Point'"""

Point = namedtuple('Point', 'x y')

"""Create an instance of Point"""

p = Point(x=10, y=20)
print(p.x)  # Outputs: 10
print(p.y)  # Outputs: 20

# Example Usage of Namedtuples
"""Let's see a more complete example:"""


"""Define a named tuple type called 'Car'"""

Car = namedtuple('Car', 'make model year')

"""Create instances of Car"""

car1 = Car(make='Toyota', model='Corolla', year=2020)
car2 = Car(make='Honda', model='Civic', year=2018)

"""Access fields by name"""

print(car1.make)  # Outputs: 'Toyota'
print(car2.model)  # Outputs: 'Civic'
print(car1.year)  # Outputs: 2020

"""Access fields by index"""

print(car1[0])  # Outputs: 'Toyota'
print(car2[1])  # Outputs: 'Civic'

"""Additional Features of Namedtuples"""

"""_fields: A tuple containing the field names:"""

print(Car._fields)  # Outputs: ('make', 'model', 'year')

"""_replace(): Creates a new instance with specified fields replaced:"""

new_car = car1._replace(year=2022)
print(new_car)  # Outputs: Car(make='Toyota', model='Corolla', year=2022)

"""_asdict(): Converts the namedtuple to a dictionary:"""

car_dict = car1._asdict()
# Outputs: {'make': 'Toyota', 'model': 'Corolla', 'year': 2020}
print(car_dict)

# Immutability and Hashability
"""Because tuples are immutable, they can be used as keys in dictionaries and added to sets:"""

# Using a tuple as a dictionary key
coordinates = {}
coordinates[(0, 0)] = "Origin"
print(coordinates)  # Outputs: {(0, 0): 'Origin'}

# Adding tuples to a set
unique_tuples = set()
unique_tuples.add((1, 2))
unique_tuples.add((1, 2))  # Duplicate, won't be added
print(unique_tuples)  # Outputs: {(1, 2)}

# Performance Benefits
"""Tuples are generally more memory-efficient and faster than lists because they are immutable:"""

import sys

list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)
print(sys.getsizeof(list_example), "Bytes")  # Size of list in Bytes
print(sys.getsizeof(tuple_example), "Bytes")  # Size of tuple in Bytes

# Using Tuples in Dictionaries and Sets
"""Tuples can be used as keys in dictionaries or elements in sets due to their immutability:"""

"""Using tuples in a dictionary"""
points = {(1, 2): "A", (3, 4): "B"}
print(points[(1, 2)])  # Outputs: "A"

"""Adding tuples to a set"""
unique_points = set()
unique_points.add((1, 2))
unique_points.add((3, 4))
print(unique_points)  # Outputs: {(1, 2), (3, 4)}