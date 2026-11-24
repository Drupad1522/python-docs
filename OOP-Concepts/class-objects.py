"""Examples of defining classes, creating objects, constructors (__init__), methods, and __str__ in Python."""

# ==============================================================================
# 1. Basic Class and Object Creation
# ==============================================================================
# A class is a user-defined blueprint / template for creating objects.
# An object is an instance of a class that contains real values.
# By convention, class names use PascalCase (CamelCase), e.g., User, PersonDetails.

class User:
    """A simple class representing a user."""
    # Class body can contain variables, functions (methods), or a pass statement
    pass

# Creating an object (instantiation)
user1 = User()
print("Created User object:", user1)
print("Type of user1:", type(user1))


# ==============================================================================
# 2. The __init__() Constructor and the 'self' Parameter
# ==============================================================================
# __init__() is a special method (constructor) called automatically when creating an object.
# 'self' refers to the current instance of the class and is used to bind attributes to that instance.

class Person:
    # Class attribute: Shared by all instances of Person
    species = "Homo sapiens"

    def __init__(self, name, age):
        # Instance attributes: Unique to each person instance
        self.name = name
        self.age = age

    # Instance method: A function defined inside a class that operates on the instance
    def introduce(self):
        """Display an introductory message for the person."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def celebrate_birthday(self):
        """Increment age by 1 and display a birthday message."""
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

    # __str__() method: Defines how the object is represented as a string
    # Called automatically by print(obj) or str(obj)
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"


# ==============================================================================
# 3. Creating Objects and Accessing Attributes
# ==============================================================================
print("\n--- Creating Person Objects ---")
# Creating instances of Person by passing arguments to __init__
person1 = Person("Drupad", 24)
person2 = Person("Ravi", 27)

# Accessing instance attributes using dot notation (.)
print(f"person1 -> Name: {person1.name}, Age: {person1.age}")
print(f"person2 -> Name: {person2.name}, Age: {person2.age}")

# Accessing class attribute (accessible via the class itself or through any instance)
print("Class attribute via class (Person.species):", Person.species)
print(f"Class attribute via instance ({person1.name}.species):", person1.species)


# ==============================================================================
# 4. Calling Instance Methods
# ==============================================================================
print("\n--- Calling Methods ---")
# Calling instance methods on objects
person1.introduce()
person2.introduce()

# Modifying state through an instance method
person1.celebrate_birthday()


# ==============================================================================
# 5. String Representation with __str__()
# ==============================================================================
# Without __str__(), print(person1) would output a memory address like <__main__.Person object at 0x...>
# With __str__(), it returns our readable formatted string:
print("\n--- String Representation (__str__) ---")
print("Printing person1 directly:", person1)
print("Printing person2 directly:", person2)


# ==============================================================================
# 6. Modifying and Deleting Attributes & Objects
# ==============================================================================
print("\n--- Modifying and Deleting Attributes ---")

# Modifying an attribute value directly
person1.age = 26
print(f"Updated {person1.name}'s age directly:", person1.age)

# Adding a new attribute dynamically to a specific instance
person1.email = "drupads1522@gmail.com"
print(f"Dynamically added email attribute to {person1.name}:", person1.email)

# Deleting an attribute using del
del person1.email
print(f"Deleted 'email' attribute. Has 'email' attribute?:", hasattr(person1, "email"))

# Deleting an object from memory using del
del person2
print("Deleted person2 object using del.")
