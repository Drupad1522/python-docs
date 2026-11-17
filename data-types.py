"""Examples of Python's built-in data types."""

# Numeric types store whole numbers, decimal numbers, and complex values.
print("Integer:")
integer_value = 5
print(integer_value, type(integer_value))

print("\nFloat:")
float_value = 5.5
print(float_value, type(float_value))

print("\nComplex:")
complex_value = 2 + 3j
print(complex_value, type(complex_value))

# Sequence types keep items in an order and support indexing.
print("\nString:")
text = "Hello, World"
print(text, type(text))
print("Character at index 7:", text[7])

print("\nList (mutable sequence):")
numbers = [1, 2, 3, 4, 3]
print(numbers, type(numbers))
print("Item at index 2:", numbers[2])

print("\nTuple (immutable sequence):")
values = ("a", "b", "c", 2, 4, 5, 1.0)
print(values, type(values))
print("Item at index 3:", values[3])

# Sets contain unique items; their display order is not guaranteed.
print("\nSet (unique items):")
unique_values = {"a", "b", "c", "b", 2, 3, 4, 2}
print(type(unique_values))
for item in unique_values:
    print(item)

# Dictionaries map keys to values. get() safely returns None for a missing key.
print("\nDictionary (key-value pairs):")
person = {1: "name", "a1": "age", "address": "Mysore"}
print(person, type(person))
print("Value for 'a1':", person["a1"])
print("Missing key:", person.get("a2"))
