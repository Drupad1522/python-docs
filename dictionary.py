"""Examples of creating, accessing, modifying, and iterating over Python dictionaries."""

# In a dictionary, data is stored as key: value pairs.
# Keys must be unique and immutable (e.g., string, number, tuple), while values can be of any data type.
dict1 = {"name": "drupad", "age": 24}
print("Dictionary created with curly braces {}:", dict1)

# The dict() constructor creates a dictionary from keyword arguments or key-value sequences.
dict2 = dict(name="drupad", age=24, email="drupads1522@gmail.com")
print("Dictionary created using dict():", dict2)

# Accessing values using a key in square brackets or using the get() method
print("\nAccessing 'name' using key index:", dict1["name"])
print("Accessing 'email' using get() method:", dict2.get("email"))

# Adding a new key-value pair
dict2["phnNo"] = "+91xxxxxxx"
print("\nAfter adding 'phnNo':", dict2)

# Updating an existing key's value
dict2["age"] = 25
print("After updating 'age':", dict2)

# Removing items from a dictionary:
# 1. del removes a specific key-value pair by key
del dict2["phnNo"]
print("\nAfter deleting 'phnNo' using del:", dict2)

# 2. pop() removes the specified key and returns its associated value
val = dict2.pop("email")
print("Value removed using pop('email'):", val)
print("Dictionary after pop():", dict2)

# 3. popitem() removes and returns the last inserted key-value pair as a tuple (key, value)
popped_item = dict2.popitem()
print("Item removed using popitem():", popped_item)
print("Dictionary after popitem():", dict2)

# 4. clear() removes all key-value pairs from the dictionary
dict2.clear()
print("Dictionary after clear():", dict2)

# Iterating through a dictionary using keys(), values(), and items()
dict3 = dict(name="drupad", age=24, email="drupads1522@gmail.com", phnNo="+91xxxxx")
print("\nOriginal dict3 for iteration:", dict3)

# Looping over a dictionary directly iterates through its keys (equivalent to dict3.keys())
print("\nIterating through keys:")
for k in dict3:  # Same as: for k in dict3.keys():
    print("Key:", k)

# Iterating through values using values()
print("\nIterating through values:")
for val in dict3.values():
    print("Value:", val)

# Iterating through key-value pairs simultaneously using items()
print("\nIterating through key-value pairs (items):")
for k, v in dict3.items():
    print(f"{k}: {v}")

# Accessing each value by looking up the key in the loop
print("\nAccessing values using keys:")
for k in dict3:
    print(f"dict3['{k}'] = {dict3[k]}")
