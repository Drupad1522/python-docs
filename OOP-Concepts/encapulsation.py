"""Examples of Encapsulation in Python: Public, Protected, and Private Access Modifiers, Name Mangling, and Getters/Setters."""

# ==============================================================================
# What is Encapsulation?
# ==============================================================================
# Encapsulation is one of the fundamental pillars of Object-Oriented Programming (OOP).
# It refers to:
# 1. Bundling data (attributes) and methods that manipulate that data into a single unit (class).
# 2. Restricting direct access to an object's internal state to prevent unauthorized or accidental modifications (Data Hiding).
#
# Access Modifiers in Python (by convention):
# - Public    : No underscore (e.g., self.name). Accessible from anywhere (inside class, outside class, subclasses).
# - Protected : Single leading underscore (e.g., self._age). By convention, intended only for internal use within the class and its subclasses.
# - Private   : Double leading underscore (e.g., self.__salary). Accessible ONLY inside the defining class (enforced via Name Mangling).


# ==============================================================================
# 1. Defining the Employee Class with Access Modifiers
# ==============================================================================

class Employee:
    """Class demonstrating public, protected, and private members."""

    def __init__(self, name, age, salary):
        # 1. Public attribute: Accessible anywhere
        self.name = name

        # 2. Protected attribute: Indicated by a single underscore '_'
        # Convention: Should only be accessed inside this class and its subclasses.
        self._age = age

        # 3. Private attribute: Indicated by a double underscore '__'
        # Cannot be accessed directly from outside the class.
        self.__salary = salary

    # Public method: Anyone can call this
    def show_details(self):
        """Display employee details safely from inside the class."""
        print(f"Employee Details -> Name: {self.name}, Age: {self._age}")
        # Private members ARE accessible from inside the class
        self.__show_salary()

    # Protected method: Intended for internal / subclass use
    def _show_age(self):
        """Protected method: displays age."""
        print(f"Protected method: Age is {self._age}")

    # Private method: Only callable from inside the Employee class
    def __show_salary(self):
        """Private method: displays salary."""
        print(f"Private method: Salary is ₹{self.__salary:,}")

    # ==========================================================================
    # 2. Getter and Setter Methods for Controlled Access
    # ==========================================================================
    # Getters and setters allow reading and modifying private attributes securely.

    def get_salary(self):
        """Getter: Safely retrieves the private salary."""
        return self.__salary

    def set_salary(self, new_salary):
        """Setter: Safely updates the private salary with input validation."""
        if new_salary > 0:
            self.__salary = new_salary
            print(f"[✓] Salary updated successfully to ₹{self.__salary:,}")
        else:
            print("[!] Invalid salary amount. Salary must be a positive number.")


print("=" * 65)
print("1. CREATING AN OBJECT AND ACCESSING MEMBERS")
print("=" * 65)

# Instantiating the Employee class with required arguments
emp = Employee("Drupad", 24, 75000)

# --- Public Members ---
print(f"Public attribute (emp.name): {emp.name}")
emp.show_details()

# --- Protected Members ---
# Python does not strictly forbid access to protected members, but it is discouraged by convention.
print(f"\nProtected attribute (emp._age): {emp._age} (Accessing is discouraged outside class)")
emp._show_age()

# --- Private Members ---
# Attempting to access a private attribute directly raises an AttributeError
print("\nAttempting to access private attribute directly (emp.__salary):")
try:
    print(emp.__salary)
except AttributeError as e:
    print(f"[x] Error: {e}")
    print("    Private attributes cannot be accessed directly from outside the class!")

# Attempting to call a private method directly also raises an AttributeError
print("\nAttempting to call private method directly (emp.__show_salary()):")
try:
    emp.__show_salary()
except AttributeError as e:
    print(f"[x] Error: {e}")


# ==============================================================================
# 3. Getters and Setters in Action (Data Validation)
# ==============================================================================
print("\n" + "=" * 65)
print("2. CONTROLLED ACCESS USING GETTERS & SETTERS")
print("=" * 65)

# Reading private salary via getter
print(f"Salary retrieved using getter: ₹{emp.get_salary():,}")

# Updating private salary via setter with valid data
emp.set_salary(85000)

# Attempting to set an invalid salary (negative number rejected by validation)
emp.set_salary(-5000)


# ==============================================================================
# 4. Name Mangling (How Python Implements Private Attributes)
# ==============================================================================
# Python does not have true private variables. Instead, it alters (mangles)
# the attribute name internally by prefixing it with '_ClassName':
# __salary becomes _Employee__salary

print("\n" + "=" * 65)
print("3. NAME MANGLING (BEHIND THE SCENES)")
print("=" * 65)

# We can access private members through their mangled names:
print("Accessing private attribute via mangled name (emp._Employee__salary):")
print(f"Salary: ₹{emp._Employee__salary:,}")

# Calling private method via mangled name:
emp._Employee__show_salary()


# ==============================================================================
# 5. Inheritance and Protected Members
# ==============================================================================
# Subclasses can freely access protected members (_age) inherited from the parent.

class Manager(Employee):
    """Subclass inheriting from Employee."""

    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display_manager_info(self):
        print(f"\nManager: {self.name} | Department: {self.department}")
        # Can access parent's protected attribute (_age)
        print(f"Protected attribute accessed in subclass (_age): {self._age}")
        # Cannot access parent's private attribute directly, but can use parent getter
        print(f"Private attribute accessed via parent getter: ₹{self.get_salary():,}")


print("\n" + "=" * 65)
print("4. SUBCLASS ACCESSING PROTECTED MEMBERS")
print("=" * 65)

mgr = Manager("Ravi", 32, 120000, "Engineering")
mgr.display_manager_info()
