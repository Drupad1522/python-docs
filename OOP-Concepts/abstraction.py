"""Examples of Abstraction in Python: Abstract Base Classes (ABC), @abstractmethod, Concrete Methods, and Abstract Properties."""

from abc import ABC, abstractmethod
import math

# ==============================================================================
# What is Abstraction?
# ==============================================================================
# Abstraction is the process of hiding internal implementation details and
# exposing only the essential interface to the user.
#
# Real-World Analogy:
# When you drive a car, you interact with the steering wheel, accelerator, and brake pedals (the interface).
# You don't need to know the inner workings of the combustion engine or fuel injection (the implementation).
#
# Key Concepts & Terminology:
# 1. Interface: Defines WHAT operations are available (method names and signatures).
# 2. Implementation: Contains the actual logic of HOW those operations are performed.
# 3. Abstract Class: A blueprint class that cannot be instantiated directly; it contains one or more abstract methods.
# 4. Abstract Method: A method declared with @abstractmethod that has no implementation in the base class and MUST be overridden by child classes.


# ==============================================================================
# 1. Abstract Base Class (ABC)
# ==============================================================================

class Shape(ABC):
    """Abstract Base Class representing a geometric shape.
    Any class inheriting from Shape MUST implement the abstract methods.
    """

    def __init__(self, color="Black"):
        # Abstract classes CAN have a constructor to initialize common attributes
        self.color = color

    # --- Abstract Methods (Must be implemented by every concrete subclass) ---
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

    # --- Abstract Property (Subclasses must provide this property) ---
    @property
    @abstractmethod
    def shape_name(self):
        """Return the name of the shape."""
        pass

    # --- Concrete Method (Fully implemented, shared by all subclasses) ---
    def describe(self):
        """A fully implemented method that uses abstract methods polymorphically."""
        return (
            f"Shape: {self.shape_name} | Color: {self.color} | "
            f"Area: {self.area():.2f} | Perimeter: {self.perimeter():.2f}"
        )


# ==============================================================================
# 2. Rule 1: Cannot Instantiate an Abstract Class Directly
# ==============================================================================
print("=" * 65)
print("1. CANNOT INSTANTIATE AN ABSTRACT CLASS DIRECTLY")
print("=" * 65)

try:
    # This raises a TypeError because Shape contains abstract methods
    generic_shape = Shape()
except TypeError as error:
    print("[x] Error caught successfully:")
    print(f"    {error}")
    print("    Rule: Python prevents direct instantiation of classes with abstract methods.")


# ==============================================================================
# 3. Concrete Subclasses Implementing the Abstract Interface
# ==============================================================================

class Rectangle(Shape):
    """Concrete subclass representing a rectangle."""

    def __init__(self, width, length, color="Blue"):
        super().__init__(color)  # Initialize parent attributes
        self.width = width
        self.length = length

    # Implementing abstract property
    @property
    def shape_name(self):
        return "Rectangle"

    # Implementing abstract method 1
    def area(self):
        return self.width * self.length

    # Implementing abstract method 2
    def perimeter(self):
        return 2 * (self.width + self.length)


class Circle(Shape):
    """Concrete subclass representing a circle."""

    def __init__(self, radius, color="Red"):
        super().__init__(color)
        self.radius = radius

    # Implementing abstract property
    @property
    def shape_name(self):
        return "Circle"

    # Implementing abstract method 1
    def area(self):
        return math.pi * (self.radius ** 2)

    # Implementing abstract method 2
    def perimeter(self):
        return 2 * math.pi * self.radius


print("\n" + "=" * 65)
print("2. CONCRETE SUBCLASSES IN ACTION")
print("=" * 65)

# Instantiating and using Rectangle
rect = Rectangle(width=4, length=5, color="Blue")
print(f"Rectangle Area: {rect.area()}")
print(f"Rectangle Perimeter: {rect.perimeter()}")
print("Calling concrete describe() method:")
print(rect.describe())

# Instantiating and using Circle
circle = Circle(radius=3, color="Red")
print(f"\nCircle Area: {circle.area():.2f}")
print(f"Circle Perimeter: {circle.perimeter():.2f}")
print("Calling concrete describe() method:")
print(circle.describe())


# ==============================================================================
# 4. Rule 2: Incomplete Subclass Enforcement
# ==============================================================================
# If a subclass fails to implement ALL abstract methods/properties,
# Python prevents it from being instantiated.

class IncompleteShape(Shape):
    """A subclass that implements area(), but forgets perimeter() and shape_name."""

    def area(self):
        return 100


print("\n" + "=" * 65)
print("3. ENFORCING THE CONTRACT: INCOMPLETE SUBCLASSES")
print("=" * 65)

try:
    incomplete = IncompleteShape()
except TypeError as error:
    print("[x] Error caught when creating IncompleteShape:")
    print(f"    {error}")
    print("    Rule: Subclasses MUST implement every single abstract method/property.")


# ==============================================================================
# 5. Polymorphic Usage of Abstract Classes
# ==============================================================================
# Callers can interact with any shape purely through the common abstract interface.

print("\n" + "=" * 65)
print("4. POLYMORPHIC PROCESSING VIA ABSTRACT INTERFACE")
print("=" * 65)

shapes = [
    Rectangle(10, 20, color="Green"),
    Circle(7, color="Yellow"),
    Rectangle(3, 8, color="Purple")
]

for s in shapes:
    # The caller relies on the guaranteed Shape contract:
    print(s.describe())
