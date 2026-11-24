"""Examples of creating, accessing, and modifying Python lists."""

# A list is an ordered collection that can contain different data types.
items = [1, 2, 3, 4.9, "abd"]
print("Original list:", items)

# The list() constructor creates a list from another iterable, such as a tuple.
numbers = list((1, 2, 3, 4))
print("List created from a tuple:", numbers)

# List indexes start at zero, so index 0 refers to the first item.
print("First item:", items[0])

# append() adds one item to the end of a list.
items.append(10)
print("After append:", items)

# insert() adds an item at the specified index.
items.insert(2, "added")
print("After insert:", items)

# extend() adds each item from an iterable to the end of the list.
items.extend(("added", "at", "last"))
print("After extend:", items)

# Lists are mutable, so an item can be replaced using its index.
items[0] = 5
print("After updating the first item:", items)
items[4]="abcd"
print("After updating the string item:", items)


#remove() is used to remove the first occurance of an element in a list
items.remove("added")
print("after removing added from a list:",items)

#pop() will remove the last element from the list
res=items.pop()
print("after poped last element from list:",items,"and poped element is:",res)

#del() it used to delete an element at specific index
del items[0]
print("after deleting value at index 0:",items)

#clear() used to remove all the elements of a list
items.clear()
print("after using clear() method:",items)

