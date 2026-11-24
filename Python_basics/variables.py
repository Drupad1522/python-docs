"""Examples of variables and object references in Python."""

# A variable name refers to an object; Python determines the object's type.
integer_value = 5
name = "Drupad"
decimal_value = 4.983
is_active = True
print(integer_value, name, decimal_value, is_active)

# Assignment copies the reference. Reassigning one name does not change another.
first = 5
second = first
print("Before reassignment:", first, second)
first = "updated"
print("After reassignment:", first, second)
