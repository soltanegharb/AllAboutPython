# Basic Usage:
"""It prints out whatever string you put inside the parentheses."""

print("Hello, World!")

# Multiple Arguments:
"""It prints "Hello" and "World!" separated by a space."""

print("Hello", "World!")

# Separator:
"""You can use the sep parameter to define a custom separator. This prints: Hello-World!"""

print("Hello", "World!", sep="-")

# End Parameter:
"""The end parameter changes the ending character. By default, it's a newline character \n. The above code prints: Hello!!!World."""

print("Hello", end="!!!")
print("World")

# Formatted Strings:
'''You can use formatted strings (f-strings) to include variables. It prints: Alice is 30 years old.'''

name = "Alice"
age = 30
print(f"{name} is {age} years old")

# File Handling:
'''You can direct the output to a file using the file parameter.'''

with open("output.txt", "w") as file:
    print("Hello, World!", file=file)

# Printing with Escape Sequences:
'''The \n escape sequence adds a new line.'''

print("Line 1\nLine 2\nLine 3")

# Printing Non-String Types:
'''You can print various data types directly.'''

print(10)           # Integer
print(3.14)         # Float
print(True)         # Boolean

# Printing Dictionary Items:
"""This prints the entire dictionary: {'name': 'Alice', 'age': 30}."""

my_dict = {"name": "Alice", "age": 30}
print(my_dict)

# Joining Lists:
'''This joins list items into a single string: apple, banana, cherry.'''

my_list = ["apple", "banana", "cherry"]
print(", ".join(my_list))

# Formatted Output Using format():
'''It prints: Bob is 25 years old.'''
name = "Bob"
age = 25
print("{} is {} years old".format(name, age))

# Printing with the % Operator:
'''This prints: Charlie is 28 years old.'''

name = "Charlie"
age = 28
print("%s is %d years old" % (name, age))

# Printing Unicode Characters:
'''This prints: Ω.'''

print("\u03A9")  # Prints the Greek capital letter Omega (Ω)

# Printing Raw Strings:
'''The r before the string makes it a raw string, which ignores escape characters.So it prints exactly as typed: This is a raw string \n with no special treatment.'''

print(r"This is a raw string \n with no special treatment")

# Printing to STDERR:
'''You can direct your output to the standard error stream, useful for logging errors separately from regular output.'''

import sys
print("This is an error message", file=sys.stderr)

# Printing with Colors (using colorama library):
'''Using external libraries like colorama, you can add colors to your printed text for better readability and emphasis.'''

from colorama import Fore, Style
print(Fore.RED + "This is red text" + Style.RESET_ALL)

# Printing Data Structures Nicely (using pprint):
'''pprint(pretty print) makes complex data structures more readable.'''

from pprint import pprint
my_data = {"name": "Alice", "age": 30, "hobbies": ["reading", "biking"]}
pprint(my_data)

# Printing JSON Formatted Data:
'''You can use the json library to print dictionaries in a well-formatted JSON style.'''

import json
data = {"name": "Bob", "age": 25, "hobbies": ["coding", "gaming"]}
print(json.dumps(data, indent=4))

# Printing with Buffering:
'''The flush parameter forces the system to print output immediately, which is useful for real-time applications.
'''

import time
import sys

for i in range(5):
    print(i, end='', flush=True)
    time.sleep(1)