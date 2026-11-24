"""Examples of creating, accessing, slicing, and modifying arrays using array.array and numpy."""

# Python does not have a native built-in array data structure.
# Instead, we can use:
# 1. 'array' module (arr.array) from the Python Standard Library - for basic typed arrays.
# 2. 'numpy' library (np.array) - a powerful third-party library for numerical computing.

# Lists vs Arrays:
# - Lists: Dynamic size, can store heterogeneous data types (e.g., ints, strings, floats mixed).
# - Arrays: Store homogeneous data types (all elements must be of the same type), memory-efficient.

import array as arr
import numpy as np

# Creating an array using the array module:
# 'i' is the typecode representing signed integers. Other common typecodes: 'f' (float), 'd' (double).
a1 = arr.array("i", [1, 2, 3, 4, 5])

# Creating an array using NumPy:
a2 = np.array([11, 12, 13, 14, 15])

print("Type of a1 (standard library):", type(a1))
print("Type of a2 (NumPy):", type(a2))

# --- Modifying elements in array.array ---

# insert(index, value) inserts an element at a specific index
a1.insert(1, 10)
print("\nAfter a1.insert(1, 10):", a1)

# append(value) adds an element to the end of the array
a1.append(100)
print("After a1.append(100):", a1)

# --- Accessing and Iterating over array elements ---

# 1. Direct iteration over elements
print("\nIterating through elements directly:")
for item in a1:
    print(item)

# 2. Iterating using index with range(len())
print("\nIterating using index:")
for i in range(len(a1)):
    print(f"Index {i}: {a1[i]}")

# 3. Iterating with both index and value using enumerate()
print("\nIterating with index and value using enumerate():")
for i, val in enumerate(a1):
    print(f"Index {i}: {val}")

# --- Removing elements ---

# remove(value) removes the first occurrence of a specific value
a1.remove(100)
print("\nAfter a1.remove(100):", a1)

# pop([index]) removes and returns the element at the specified index;
# if no index is given, it removes and returns the last element.
popped_last = a1.pop()
print("Popped last element (a1.pop()):", popped_last)

popped_first = a1.pop(0)
print("Popped element at index 0 (a1.pop(0)):", popped_first)
print("Array after pops:", a1)

# --- Slicing arrays (using NumPy array a2) ---

# Slicing from the beginning up to index 4 (exclusive): [:4]
print("\nSlicing a2 up to index 4 (a2[:4]):", a2[:4])

# Reversing an array using negative step [::-1]
print("Reversed a2 using slicing (a2[::-1]):", a2[::-1])

# --- Additional methods in array.array ---

# index(value) returns the index of the first occurrence of a value
print("\nIndex of 10 in a1 (a1.index(10)):", a1.index(10))

# count(value) returns the number of occurrences of a value in the array
print("Count of 2 in a1 (a1.count(2)):", a1.count(2))

# reverse() reverses the array in-place (modifies the array directly and returns None)
a1.reverse()
print("After a1.reverse():", a1)

# extend(iterable) appends items from an iterable to the end of the array in-place (returns None)
a1.extend([9, 8, 6, 7])
print("After a1.extend([9, 8, 6, 7]):", a1)
