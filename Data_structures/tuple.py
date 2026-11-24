"""Examples of creating, accessing, and using Python tuples."""

# A tuple is an ordered collection that can contain different data types.
items = (1, 2, 3, 4.9, "hello")
print("Original tuple:", items)

# The tuple() constructor creates a tuple from another iterable, such as a list.
values = tuple([1, 2, 3, 4, "hello"])
print("Tuple created from a list:", values)

# Tuple indexes start at zero, so index 0 refers to the first item.
print("First item:", items[0])

# Tuples support slicing to access a range of items.
print("First three items:", items[:3])
print("Every second item:", items[::2])
print("Items in reverse order:", items[::-1])

# The + operator combines tuples into a new tuple.
more_items = ("world", "!")
combined = items + more_items
print("Combined tuple:", combined)

# Tuples are immutable, so their items cannot be changed after creation.
# Use del to remove a tuple variable when it is no longer needed.
del values
