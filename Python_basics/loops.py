"""Examples of repeating work with for and while loops."""

# range(start, stop, step) produces integers up to, but not including, stop.
print("For loop over a range:")
for number in range(0, 4, 1):
    print(number)

# Iterate over the values directly when indexes are not needed.
items = ["a", "b", 2, 54, 7.098]
print("\nFor loop over list values:")
for item in items:
    print(item)

# Use range(len(...)) when an index is needed; enumerate is often clearer.
print("\nList indexes and values with enumerate:")
for index, item in enumerate(items):
    print(index, item)

# A while loop continues as long as its condition is true.
print("\nWhile loop countdown:")
count = 3
while count > 0:
    print(count)
    count -= 1
