"""Examples of creating, modifying, and using Python sets and set operations."""

# A set is an unordered collection of unique elements.
# Sets are mutable, but their elements must be immutable (hashable) and can be heterogeneous.
s = {10, 20, 30}
print("Set created with curly braces {}:", s)

# The set() constructor creates a set from any iterable (list, tuple, dict, range, string, etc.).
s1 = set([1, 2, 3, 4])
s2 = set((1, 2, 3, 4))
s3 = set({1: 10, 2: 20, 3: 30})  # When a dictionary is passed, only its keys are added to the set
s4 = set(range(0, 5))
s5 = set("hello")  # Duplicate characters ('l') are automatically removed

print("Set created from list:", s1)
print("Set created from tuple:", s2)
print("Set created from dictionary keys:", s3)
print("Set created from range:", s4)
print("Set created from string:", s5)

# Methods for modifying sets:
# 1. add() inserts a single element into the set
s.add(40)
print("\nAfter s.add(40):", s)

# If we attempt to add a duplicate value, the set ignores it
s.add(30)
print("After adding duplicate 30 (ignored):", s)

# 2. remove() removes a specified element; raises a KeyError if the element is not found
s.remove(40)
print("\nAfter s.remove(40):", s)

# 3. discard() removes a specified element without raising an error if it does not exist
s.discard(100)
print("After s.discard(100) (element not present, safely ignored):", s)

# Set operations: union, intersection, difference, and symmetric difference
s1 = {1, 2, 3, 4, 5}
s2 = {5, 6, 7, 8, 9}
print("\nSet s1:", s1)
print("Set s2:", s2)

# union() or '|' combines and returns all unique elements from both sets
print("\nUnion using union():", s1.union(s2))
print("Union using '|' operator:", s1 | s2)

# intersection() or '&' returns elements common to both sets
print("\nIntersection using intersection():", s1.intersection(s2))
print("Intersection using '&' operator:", s1 & s2)

# difference() or '-' returns elements present in the first set but not in the second set
print("\nDifference s1.difference(s2) (in s1 but not in s2):", s1.difference(s2))
print("Difference s2.difference(s1) (in s2 but not in s1):", s2.difference(s1))
print("Difference using '-' operator (s1 - s2):", s1 - s2)

# symmetric_difference() or '^' returns elements present in either set, but not both
print("\nSymmetric difference s1.symmetric_difference(s2):", s1.symmetric_difference(s2))
print("Symmetric difference using '^' operator:", s1 ^ s2)
