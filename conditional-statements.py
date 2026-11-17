"""Examples of choosing which code to run with conditional statements."""

# Read one age so each example can reuse the same value.
age = int(input("Enter your age: "))

# if-else: choose between two outcomes.
print("\nIf-else statement:")
if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

# if-elif-else: choose one outcome from several ranges.
print("\nIf-elif-else statement:")
if age <= 12:
    print("Child")
elif age <= 18:
    print("Young adult")
else:
    print("Adult")

# Nested if statements: check a second condition inside the first branch.
print("\nNested if statement:")
if age <= 12:
    if age <= 1:
        print("Infant")
    elif age <= 8:
        print("Child aged 2 to 8")
    else:
        print("Child aged 9 to 12")
elif age <= 18:
    print("Person aged 13 to 18")
else:
    print("Adult")

# match-case is available in Python 3.10 and later.
# Uncomment this example to try matching age ranges with guards.
# match age:
#     case n if n <= 1:
#         print("Infant")
#     case n if n <= 8:
#         print("Child aged 2 to 8")
#     case n if n <= 12:
#         print("Child aged 9 to 12")
#     case n if n <= 18:
#         print("Young adult")
#     case _:
#         print("Adult")
