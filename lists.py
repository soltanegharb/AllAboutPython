# Creating Lists
"""You can create a list by enclosing elements in square brackets []:"""

from collections import Counter
import copy
from collections import deque
import itertools
import bisect
my_list = [1, 2, 3, 4, 5]

"""The list() function is a built-in Python function that creates a list object. Lists are one of the most commonly used data types in Python, and they're very flexible."""

# Creating an Empty List:

empty_list = list()
print(empty_list)  # Outputs: []

# Converting Other Iterables to List
"""You can convert other iterable types (like tuples, strings, or sets) into a list."""

tuple_example = (1, 2, 3)
list_from_tuple = list(tuple_example)
print(list_from_tuple)  # Outputs: [1, 2, 3]

set_example = {1, 2, 3}
list_from_set = list(set_example)
print(list_from_set)  # Outputs: [1, 2, 3]

string_example = 'hello'
list_from_string = list(string_example)
print(list_from_string)  # Outputs: ['h', 'e', 'l', 'l', 'o']

# Accessing Elements
"""You can access elements by their index (starting from 0):
"""
my_list = [1, 2, 3]
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

# Multiplying Lists:
"""Repeat the elements of a list."""

my_list = [1, 2, 3]
multiplied = my_list * 3
print(multiplied)  # Outputs: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Modifying Elements
"""You can modify elements using their index:"""

my_list = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

# List Methods
"""Append: Adds an element to the end of the list."""

my_list = [1, 2, 10, 4, 5]
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

"""Insert: Inserts an element at a specified position."""

my_list = [1, 2, 10, 4, 5, 6]
my_list.insert(2, 15)
print(my_list)  # Output: [1, 2, 15, 10, 4, 5, 6]

"""Remove: Removes the first occurrence of an element."""

my_list = [1, 2, 15, 10, 4, 5, 6]
my_list.remove(10)
print(my_list)  # Output: [1, 2, 15, 4, 5, 6]

"""Pop: Removes and returns the element at a specified position."""

my_list = [1, 2, 15, 4, 5, 6]
popped_element = my_list.pop(3)
print(popped_element)  # Output: 4
print(my_list)  # Output: [1, 2, 15, 5, 6]

"""Sort: Sorts the list in ascending order."""

my_list = [1, 2, 15, 5, 6]
my_list.sort()
print(my_list)  # Output: [1, 2, 5, 6, 15]

"""Reverse: Reverses the order of the list."""

my_list = [1, 2, 5, 6, 15]
my_list.reverse()
print(my_list)  # Output: [15, 6, 5, 2, 1]

"""Extending a List:"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Outputs: [1, 2, 3, 4, 5, 6]

# Checking if List is Empty:
"""Using a simple condition to check."""

my_list = []
print(not my_list)  # Outputs: True (list is empty)

# Finding the Maximum and Minimum:
"""Simple methods to find max and min values."""

my_list = [10, 20, 30, 40]
print(max(my_list))  # Outputs: 40
print(min(my_list))  # Outputs: 10

# Summing Elements:
"""Using sum() to find the total of all elements."""

my_list = [10, 20, 30, 40]
print(sum(my_list))  # Outputs: 100

# Copying Lists:

original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # Outputs: [1, 2, 3]

"""Using the list() function to copy a list."""

original_list = [1, 2, 3]
copied_list = list(original_list)
print(copied_list)  # Outputs: [1, 2, 3]

# Slicing
"""You can slice lists to get a sublist:"""

sub_list = my_list[1:4]
print(sub_list)  # Output: [6, 5, 2]

# List Slicing with Steps:
"""Grab elements with a specific step."""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[1:8:2])  # Outputs: [1, 3, 5, 7]

# List Slicing to Reverse:
"""Quick way to reverse a list."""

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # Outputs: [5, 4, 3, 2, 1]

# Partitioning a List:
"""Splitting a list into chunks."""

my_list = [1, 2, 3, 4, 5, 6]
chunk_size = 2
partitioned_list = [my_list[i:i + chunk_size]
                    for i in range(0, len(my_list), chunk_size)]
print(partitioned_list)  # Outputs: [[1, 2], [3, 4], [5, 6]]

# Finding the Length:

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Outputs: 5

# List Comprehensions
"""Python allows for more concise lists creation using list comprehensions:"""

squares = [x**2 for x in range(6)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25]

# List Comprehensions with Multiple Loops:

pairs = [(x, y) for x in range(3) for y in range(3)]
# Outputs: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
print(pairs)

# List Generators:
"""Similar to list comprehensions but using generator syntax to create a generator object."""

gen = (x**2 for x in range(5))
print(list(gen))  # Outputs: [0, 1, 4, 9, 16]

# Filtering Lists:

even_squares = [x for x in squares if x % 2 == 0]
print(even_squares)  # Outputs: [0, 4, 16]

# List Comprehensions with Conditional Logic:

filtered_list = [x if x % 2 == 0 else 'odd' for x in range(10)]
# Outputs: ['even', 1, 'even', 3, 'even', 5, 'even', 7, 'even', 9]
print(filtered_list)

"""Combining List with Other Functions:"""

numbers = [1, 2, 3, 4]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Outputs: [2, 4]

# Combining Lists
"""You can concatenate two lists using the + operator:"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# Merging and Combining Lists:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [*list1, *list2]
print(merged)  # Outputs: [1, 2, 3, 4, 5, 6]
print([x for x in list1] + [x for x in list2])  # The same as upper line

# Sorting Lists:
"""Returns a new list and leaves the original list unchanged."""
unsorted_list = [3, 1, 4, 2]
sorted_list = sorted(unsorted_list)
print(sorted_list)  # Outputs: [1, 2, 3, 4]

# Using bisect for Sorted Lists:
"""Maintain a sorted list and insert elements in the correct position."""


sorted_list = [1, 3, 4, 7]
bisect.insort(sorted_list, 5)
print(sorted_list)  # Outputs: [1, 3, 4, 5, 7]

# Using itertools for Advanced List Manipulation:
"""combinations: Generate all possible combinations of a specified length."""

list1 = [1, 2, 3]
combos = list(itertools.combinations(list1, 2))
print(combos)  # Outputs: [(1, 2), (1, 3), (2, 3)]

"""permutations: Generate all possible orderings."""
perms = list(itertools.permutations(list1))
# Outputs: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(perms)

# Nested Lists:
"""Lists within lists."""

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # Outputs: 6

# List of Lists(Matrix):
"""Creating and accessing elements in a 2D list."""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Outputs: 6

# Transposing a Matrix:
"""Using zip to transpose rows and columns."""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = list(zip(*matrix))
print(transposed)  # Outputs: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# Flattening a Nested List:

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Flattening a List of Lists Using sum():

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = sum(nested_list, [])
print(flattened)  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8]

# itertools.chain:
"""The chain function takes multiple iterables (e.g., lists, tuples) and returns a single iterable that produces elements from the first input iterable until it's exhausted, then moves on to the next input iterable, and so on.
Essentially, it concatenates multiple iterables."""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = itertools.chain(list1, list2)
print(list(chained))  # Outputs: [1, 2, 3, 4, 5, 6]

# itertools.chain.from_iterable:
"""The from_iterable class method of chain is used for flattening an iterable of iterables into a single iterable.
It works by taking an iterable containing other iterables and then producing elements from each of those iterables in sequence."""

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = list(itertools.chain.from_iterable(nested_list))
print(flattened)  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8]

"""chain is great when you have distinct iterables you want to concatenate, while chain.from_iterable is perfect for flattening nested iterables. These tools can make your data manipulation tasks much more efficient and concise."""

# Flattening a Nested List (Advanced):
"""In this example, chain.from_iterable(nested_list) takes each sublist within nested_list and chains their elements together into a single sequence, which we convert into a list using list()."""

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flattened = list(itertools.chain.from_iterable(nested_list))
print(flattened)  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9]

flattened2 = list(itertools.chain(
    nested_list[0], nested_list[1], nested_list[2]))
print(flattened2)  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Flatten a List with Mixed Nested Levels:
"""A recursive function to handle varying depths."""


def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


nested_list = [1, [2, [3, 4], 5], 6]
flattened = flatten(nested_list)
print(flattened)  # Outputs: [1, 2, 3, 4, 5, 6]


# Using List as Stack:

stack = []
stack.append('a')
stack.append('b')
print(stack.pop())  # Outputs: 'b'
print(stack.pop())  # Outputs: 'a'

# Using List as Queue:

queue = deque([1, 2, 3])
queue.append(4)
print(queue.popleft())  # Outputs: 1
print(queue.popleft())  # Outputs: 2

# Enumerating Lists:

my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(index, value)
# Outputs:
# 0 a
# 1 b
# 2 c

# Zipping Lists:
"""Combine elements from multiple lists into tuples."""

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)  # Outputs: [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzipping Lists:

zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*zipped)
print(list1)  # Outputs: (1, 2, 3)
print(list2)  # Outputs: ('a', 'b', 'c')

# All and Any Functions:

numbers = [2, 4, 6, 8]
# Outputs: True (all numbers are even)
print(all(num % 2 == 0 for num in numbers))
# Outputs: True (at least one number is greater than 5)
print(any(num > 5 for num in numbers))

# Using map() with Lists:
"""Apply a function to all items in a list."""

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Outputs: [1, 4, 9, 16]

# Removing Duplicates:

my_list = [1, 2, 2, 3, 3, 3]
unique_list = list(set(my_list))
print(unique_list)  # Outputs: [1, 2, 3]

# Deepcopy Lists:
"""When you want to copy a list containing other lists(nested lists) to ensure the inner lists are also copied."""

original = [[1, 2], [3, 4]]
copied = copy.deepcopy(original)
copied[0][0] = 99
print(original)  # Outputs: [[1, 2], [3, 4]]
print(copied)    # Outputs: [[99, 2], [3, 4]]

# List Indexing with Conditions:
"""The next() function in Python is used to retrieve the next item from an iterator. The syntax next(iterator, default) allows you to provide a default value that is returned if the iterator is exhausted (i.e., if there are no more items to retrieve)."""
my_list = [10, 20, 30, 40]
index = next((i for i, x in enumerate(my_list) if x > 25), None)
print(index)  # Outputs: 2 (index of the first element greater than 25)

# Splitting a List into Head and Tail:
"""Separate the first element from the rest."""

my_list = [1, 2, 3, 4]
head, *tail = my_list
print(head)  # Outputs: 1
print(tail)  # Outputs: [2, 3, 4]

# Using Counter for Frequency Counting:
"""Count frequencies of elements in a list."""

my_list = [1, 2, 2, 3, 3, 3]
frequency = Counter(my_list)
print(frequency)  # Outputs: Counter({3: 3, 2: 2, 1: 1})
