"""Examples of Inheritance in Python: Single, Multilevel, Hierarchical, and Multiple Inheritance."""

# ==============================================================================
# What is Inheritance?
# ==============================================================================
# Inheritance allows a class (Child / Subclass / Derived class) to inherit
# attributes and methods from another class (Parent / Superclass / Base class).
# Key Benefits:
# 1. Code Reusability: Common properties and behaviors are written once in the parent.
# 2. Extensibility: Child classes can add new features or customize existing ones.


# ==============================================================================
# 1. Single Inheritance & super()
# ==============================================================================
# Single Inheritance: One child class inherits from one parent class.

class Vehicle:
    """Parent / Base class representing a general vehicle."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        """Display general vehicle details."""
        print(f"Vehicle Brand: {self.brand}, Model: {self.model}")

    def start_engine(self):
        """Generic vehicle engine start."""
        print(f"{self.brand} {self.model}: Engine started.")


class Car(Vehicle):
    """Child / Subclass inheriting from Vehicle."""

    def __init__(self, brand, model, seating_capacity=5):
        # super().__init__() invokes the parent class constructor to set brand and model
        super().__init__(brand, model)
        # Child-specific attribute
        self.seating_capacity = seating_capacity

    # Method Overriding: Re-defining a parent method to provide child-specific behavior
    def display_info(self):
        # super().display_info() calls the parent class version first
        super().display_info()
        print(f"Type: Car | Seating Capacity: {self.seating_capacity} passengers")

    # Child-specific method
    def car_info(self):
        """Informational method specific to cars."""
        print(f"{self.brand} {self.model} is a comfortable {self.seating_capacity}-seater car.")


print("=" * 60)
print("1. SINGLE INHERITANCE (Vehicle -> Car)")
print("=" * 60)

# Creating an instance of the Child class
my_car = Car("Toyota", "Hyryder", seating_capacity=5)

# 1. Calling an inherited method from Vehicle
my_car.start_engine()

# 2. Calling an overridden method (executes Car's display_info)
my_car.display_info()

# 3. Calling a child-specific method
my_car.car_info()


# ==============================================================================
# 2. Multilevel Inheritance
# ==============================================================================
# Multilevel Inheritance: A class inherits from a child class (Grandchild -> Child -> Parent).
# Hierarchy: Vehicle -> Car -> ElectricCar

class ElectricCar(Car):
    """Grandchild class inheriting from Car (and indirectly from Vehicle)."""

    def __init__(self, brand, model, seating_capacity, battery_kwh):
        super().__init__(brand, model, seating_capacity)
        self.battery_kwh = battery_kwh

    # Overriding start_engine for electric vehicles
    def start_engine(self):
        print(f"{self.brand} {self.model}: Powered ON silently (Electric Battery: {self.battery_kwh} kWh).")

    def charge_battery(self):
        """Method specific to ElectricCar."""
        print(f"{self.brand} {self.model}: Charging battery to 100%...")


print("\n" + "=" * 60)
print("2. MULTILEVEL INHERITANCE (Vehicle -> Car -> ElectricCar)")
print("=" * 60)

ev = ElectricCar("Tata", "Nexon EV", 5, 40.5)
ev.display_info()     # Inherited through Car and Vehicle
ev.start_engine()     # Overridden in ElectricCar
ev.charge_battery()   # Specific to ElectricCar


# ==============================================================================
# 3. Hierarchical Inheritance
# ==============================================================================
# Hierarchical Inheritance: Multiple child classes inherit from the same parent.
# Hierarchy: Vehicle -> Car and Vehicle -> Motorcycle

class Motorcycle(Vehicle):
    """Another child class inheriting directly from Vehicle."""

    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def do_wheelie(self):
        """Method specific to Motorcycle."""
        print(f"{self.brand} {self.model} ({self.engine_cc}cc) is performing a wheelie!")


print("\n" + "=" * 60)
print("3. HIERARCHICAL INHERITANCE (Vehicle -> Car & Motorcycle)")
print("=" * 60)

bike = Motorcycle("Yamaha", "R15", 155)
bike.display_info()   # Inherited from Vehicle
bike.start_engine()   # Inherited from Vehicle
bike.do_wheelie()     # Specific to Motorcycle


# ==============================================================================
# 4. Multiple Inheritance
# ==============================================================================
# Multiple Inheritance: A child class inherits from more than one parent class.

class Camera:
    """Parent class 1."""
    def take_photo(self):
        print("Camera: Photo captured with high resolution.")


class Phone:
    """Parent class 2."""
    def make_call(self, number):
        print(f"Phone: Calling {number}...")


class Smartphone(Camera, Phone):
    """Child class inheriting from both Camera and Phone."""
    def browse_internet(self):
        print("Smartphone: Browsing internet on 5G network...")


print("\n" + "=" * 60)
print("4. MULTIPLE INHERITANCE (Camera + Phone -> Smartphone)")
print("=" * 60)

phone = Smartphone()
phone.make_call("+919876543210")  # Inherited from Phone
phone.take_photo()                # Inherited from Camera
phone.browse_internet()           # Specific to Smartphone


# ==============================================================================
# 5. Type Checking: isinstance() and issubclass()
# ==============================================================================
# Built-in functions to verify inheritance relationships:
# - isinstance(object, Class): Checks if an object belongs to a class or its ancestors.
# - issubclass(ChildClass, ParentClass): Checks if a class is derived from another.

print("\n" + "=" * 60)
print("5. TYPE CHECKING: isinstance() & issubclass()")
print("=" * 60)

print(f"Is 'my_car' an instance of Car?: {isinstance(my_car, Car)}")
print(f"Is 'my_car' an instance of Vehicle?: {isinstance(my_car, Vehicle)}")
print(f"Is 'ev' an instance of Vehicle?: {isinstance(ev, Vehicle)}")
print(f"Is 'bike' an instance of Car?: {isinstance(bike, Car)}")

print(f"\nIs Car a subclass of Vehicle?: {issubclass(Car, Vehicle)}")
print(f"Is ElectricCar a subclass of Vehicle?: {issubclass(ElectricCar, Vehicle)}")
print(f"Is Motorcycle a subclass of Car?: {issubclass(Motorcycle, Car)}")
print(f"Is Smartphone a subclass of Camera and Phone?: {issubclass(Smartphone, (Camera, Phone))}")
