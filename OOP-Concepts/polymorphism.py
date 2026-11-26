"""Examples of Polymorphism in Python: Method Overriding, Method Overloading, Duck Typing, and Operator Overloading."""

# ==============================================================================
# What is Polymorphism?
# ==============================================================================
# Polymorphism comes from Greek: "poly" (many) and "morph" (forms).
# It means the same method, function, or operator behaves differently based on
# the object or data type it is operating on.
#
# Real-world analogy:
# A single process_payment() function can handle CreditCard, DebitCard, or UPI
# transactions differently depending on the specific payment object passed to it.


# ==============================================================================
# 1. Compile-Time Polymorphism / Method Overloading
# ==============================================================================
# In languages like Java or C++, method overloading allows defining multiple
# methods with the same name but different parameter types or counts.
#
# Python does NOT support traditional method overloading directly; defining a
# method multiple times simply overwrites the previous definition.
# Instead, Python achieves overloading using:
#   1. Variable-length arguments (*args, **kwargs)
#   2. Default parameter values (e.g., param=None)

class Calculator:
    """Demonstrating method overloading using variable-length arguments (*args)."""

    def add(self, *numbers):
        """Add any quantity of numbers passed as arguments."""
        return sum(numbers)


print("=" * 60)
print("1. METHOD OVERLOADING (SIMULATED VIA *args)")
print("=" * 60)

calc = Calculator()
print("calc.add(5):", calc.add(5))
print("calc.add(5, 10):", calc.add(5, 10))
print("calc.add(5, 10, 10):", calc.add(5, 10, 10))


# ==============================================================================
# 2. Run-Time Polymorphism / Method Overriding
# ==============================================================================
# Method Overriding: When a subclass provides its own specific implementation
# of a method that is already defined in its superclass (parent class).
#
# The method to be executed is resolved dynamically at runtime based on the
# actual object type.

class Animal:
    """Base parent class."""
    def sound(self):
        print("Animal makes a generic sound.")


class Dog(Animal):
    """Subclass overriding sound()."""
    def sound(self):
        print("Dog barks: Woof! Woof!")


class Cat(Animal):
    """Subclass overriding sound()."""
    def sound(self):
        print("Cat meows: Meow! Meow!")


print("\n" + "=" * 60)
print("2. RUN-TIME POLYMORPHISM / METHOD OVERRIDING")
print("=" * 60)

# A list of different animal objects sharing the same interface
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    # Calling the same method name produces different outputs based on object type
    animal.sound()


# ==============================================================================
# 3. Duck Typing (Polymorphism without Inheritance)
# ==============================================================================
# "If it walks like a duck and quacks like a duck, it's a duck."
# In Python, an object's suitability is determined by the presence of certain
# methods and properties, rather than its inheritance hierarchy.

class Pen:
    def use(self):
        return "Writing notes with ink."


class Eraser:
    def use(self):
        return "Erasing pencil marks."


def perform_task(tool):
    """Polymorphic function: works with ANY object that implements a use() method."""
    print(f"Tool in action: {tool.use()}")


print("\n" + "=" * 60)
print("3. DUCK TYPING (Polymorphism without Inheritance)")
print("=" * 60)

perform_task(Pen())
perform_task(Eraser())


# ==============================================================================
# 4. Polymorphism in Operators & Built-in Functions
# ==============================================================================
# Built-in functions and operators change their behavior depending on operands.

print("\n" + "=" * 60)
print("4. POLYMORPHISM IN OPERATORS & BUILT-IN FUNCTIONS")
print("=" * 60)

# The '+' operator behaves differently for numbers, strings, and lists:
# - For numbers: performs arithmetic addition
# - For strings: performs string concatenation
# - For lists: performs list merging / concatenation
print("Arithmetic Addition (5 + 10):", 5 + 10)
print("String Concatenation ('Hi' + 'hello'):", "Hi" + "hello")
print("List Concatenation ([1, 2] + [3, 4]):", [1, 2] + [3, 4])

# Built-in function polymorphism: len()
print("\nlen('Python') (string length):", len("Python"))
print("len([10, 20, 30]) (list length):", len([10, 20, 30]))
print("len({'a': 1, 'b': 2}) (dict length):", len({"a": 1, "b": 2}))
