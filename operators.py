"""Examples of common Python operators."""

# Arithmetic operators calculate with numeric values.
left = 10
right = 5
print("Arithmetic operators:")
print("Addition:", left + right)
print("Subtraction:", right - left)
print("Multiplication:", left * right)
print("Division:", left / right)          # Always produces a float.
print("Floor division:", left // right)  # Drops the fractional part.
print("Modulus:", left % right)           # Returns the remainder.

# Comparison operators return True or False.
print("\nComparison operators:")
x = 5
y = 2
print(x > y, x < y, x >= y, x <= y, x != y, x == y)

# == compares values; is checks whether two names refer to the same object.
print("\nValue equality and object identity:")
first = [1, 2]
second = [1, 2]
alias = first
print("first == second:", first == second)
print("first is second:", first is second)
print("first is alias:", first is alias)

# Logical operators combine or invert Boolean expressions.
print("\nLogical operators:")
is_ready = True
has_error = False
print(is_ready and has_error)
print(is_ready or has_error)
print(not is_ready)

# Bitwise operators work on the binary representation of integers.
print("\nBitwise operators:")
p = 5
q = 2
print("AND:", p & q)
print("OR:", p | q)
print("NOT:", ~p, ~q)

# Membership operators check whether a value occurs in a collection.
print("\nMembership operators:")
values = [1, 2, 3, 4, 5]
message = "Hello, World!"
print(10 in values)
print(2 in values)
print("w" in message)
print("W" in message)
