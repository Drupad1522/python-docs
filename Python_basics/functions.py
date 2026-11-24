"""Examples of defining and calling Python functions."""


# A function without parameters performs a simple action.
def welcome_fun():
    """Print a welcome message."""
    print("Welcome!")


welcome_fun()


# Parameters can have default values, used when an argument is omitted.
def show_values(x, y=50):
    """Display two values; y defaults to 50."""
    print("x:", x)
    print("y:", y)


show_values(100)
show_values(100, 5)


# Positional arguments are assigned by order; keyword arguments use names.
def show_info(name, age):
    """Display a person's name and age."""
    print("Name:", name)
    print("Age:", age)


print("Calling with positional arguments:")
show_info("Ravi", 27)

print("\nCalling with keyword arguments:")
show_info(name="Ravi", age=27)
show_info(age=27, name="Ravi")
