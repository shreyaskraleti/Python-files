"""Encapsulation is a fundamental concept in object-oriented programming (OOP) that restricts
direct access to certain parts of an object and allows controlled access through specific methods.
It is a way to bundle data (attributes) and methods (functions) that operate on that data into a single unit,
usually a class, and to hide the internal state of the object from the outside.

Key Aspects of Encapsulation:
Data Hiding: Internal data and methods are hidden from outside access.
Only methods that are explicitly provided by the class (like getters and setters) can interact with
these private attributes. This prevents unintended modifications and keeps the data secure.

Controlled Access: Encapsulation provides controlled access to an object's attributes and methods,
usually through public methods that act as an interface. For instance, getter and setter methods
allow safe interaction with private data.

Modularity and Flexibility: Because the internal implementation is hidden, changes to the internal
workings of the class won’t affect external code as long as the interface (public methods) remains the same.
This makes the code more modular and easier to maintain.

Example:
Consider the Person class with an encapsulated _age attribute:

_age is encapsulated (private) within the class.
get_age() and set_age() methods provide controlled access to _age.
Encapsulation thus ensures that _age can only be accessed and modified through specific methods, adding a layer of security and control over how the data is handled."""


"""A private attribute in Python is an attribute of a class that is intended to be used only within the class
itself and is not meant to be accessed directly from outside the class.
In Python, a common convention to make an attribute private is to prefix it with an underscore (_ or __).

Example of Private Attributes:
_attribute: This is a weakly private attribute, meaning it’s more of a convention to suggest it’s for internal use.
Other parts of the code can technically still access it, but the underscore signals it should not be accessed directly.

__attribute: This is a strongly private attribute.
Python "name-mangles" it to make it harder to access from outside the class.
In practice:

Private attributes help encapsulate the data, keeping it safe from unintended modifications.
Accessing or modifying private attributes directly from outside the class is discouraged.

Instead, getter and setter methods are provided to interact with them in a controlled way.

Example:
In the class Person from before, _age is a private attribute:"""


"""1. Create a class Person with a private attribute _age. Implement a method get_age() to
access the value of _age and set_age() to modify the value while keeping the attribute
private. """


class Person:
    def __init__(self, age=0):
        self._age = age  # Private attribute

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("age cannot be negative")


p1 = Person()
print(p1.get_age())
p1.set_age(25)
print(p1.get_age())

"""2. Create a class Employee with a private attribute __salary. Verify how Python handles
name mangling by accessing the private attribute using _Employee__salary. """


class Employee:
    def __init__(self, salary=0):
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary  # Getter method for __salary


e1 = Employee(20000)
# Accessing the private attribute using the getter method
print(e1.get_salary())
# Accessing the private attribute directly with name mangling
print(e1._Employee__salary)

"""3. Implement a class Product with a private attribute _price. Create getter and setter
methods using Python's property decorator to access and modify the price with validation
(e.g., price can't be negative). """

"""@property is used to define price as a property, allowing access through product.price
instead of product.get_price().
@price.setter defines the setter method for price, with a validation to ensure the price cannot be negative."""

"""In the Product class example, the price attribute is initially set to 0 in the constructor (__init__) as a default value. This is a common approach to provide a safe default for attributes that require validation.

Here are the main reasons for setting the initial value of _price to 0:

Default Initialization: By setting _price to 0, we ensure that the attribute has a default value. This helps prevent errors if a price is not provided during object creation.

Validation Consistency: If we enforce that price cannot be negative, starting at 0 (a neutral, valid value) helps keep the value within an acceptable range. A negative initial value would violate our own validation rule.

Practical Default: In many cases, defaulting price to 0 makes sense as a placeholder until a valid price is set."""


class Product:
    def __init__(self, price=0):
        self._price = price          # Private attribute

    @property
    def price(self):  # Getter method for price.
        return self._price

    @price.setter
    def price(self, value):       # Setter method for price with validation.
        if value >= 0:              # Validation to ensure price cannot be negative
            self._price = value
        else:
            raise ValueError("price cannot be negative")


p1 = Product()
print(p1.price)
p1.price = 200
print(p1.price)
try:
    p1.price = -50
except ValueError as e:
    print(e)

"""4. Define a class Circle with a private attribute _radius and create a read-only property
radius that allows getting but not setting the value directly. """
"""The @property decorator creates a read-only property for radius, allowing only the retrieval of
_radius without providing a setter.
When attempting to assign a value directly to c1.radius, an AttributeError is raised,
indicating that the property is read-only."""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius  # Getter method for radius, read-only property


c1 = Circle(10)
print(c1.radius)  # Accessing the radius property
try:
    c1.radius = 20  # Attempting to set the radius property directly
except AttributeError as e:
    print(e)  # Output: can't set attribute

"""5. Create a class BankAccount with both a protected attribute _balance and a private
attribute __pin. Implement methods to access and modify both attributes, explaining the
difference between protected and private access. """

"""The main difference between protected and private attributes in Python lies in the level of access 
restriction they imply and how they are intended to be used within and outside of a class.

Protected Attributes
Syntax: In Python, protected attributes are defined with a single underscore prefix, like _attribute.
Access Restriction: Protected attributes are intended for internal use within the class and any subclasses. 
They can technically be accessed directly from outside the class, but this goes against convention.
Usage: Protected attributes are meant to signal that they should not be accessed or modified directly from 
outside the class or subclass, although this is still possible. 
They are used in scenarios where subclasses need to access the attribute but direct access from unrelated external code is discouraged.

Private Attributes
Syntax: Private attributes are defined with a double underscore prefix, like __attribute.
Access Restriction: Private attributes are more strictly restricted than protected ones. 
Python "name-mangles" these attributes, effectively changing the attribute name internally to _ClassName__attribute, 
making them harder to access from outside the class.
Usage: Private attributes are intended to be fully encapsulated within the class, meaning they 
should not be accessed or modified from outside the class, even by subclasses. 
They provide a stronger form of data hiding, often used for sensitive information (like passwords or PINs) 
that should be accessed only through specific getter and setter methods."""


class BankAccount:
    def __init__(self, balance=0, pin=1234):
        self._balance = balance  # Protected attribute
        self.__pin = pin  # Private attribute
    # Getter for balance (protected attribute)

    def get_balance(self):
        return self._balance
    # Setter for balance (protected attribute)

    def set_balance(self, amount):
        if amount > 0:
            self._balance = amount
        else:
            print("balance cannot be negative")
    # Getter for pin (private attribute)

    def get_pin(self):
        return self.__pin
    # Setter for pin (private attribute)

    def set_pin(self, new_pin):
        if isinstance(new_pin, int) and len(str(new_pin)) == 4:
            self.__pin = new_pin
        else:
            print("Invalid PIN. Please enter a 4-digit number.")


account = BankAccount(balance=5000, pin=2345)
print(account.get_balance())
print(account.get_pin())
account.set_balance(2000)
print(account.get_balance())
account.set_pin(2543)
print(account.get_pin())

"""Explanation of Each Part
isinstance(new_pin, int):

This part checks if new_pin is an integer.
If new_pin is not an integer (for example, if it’s a string or a float), this condition will be False, 
and the assignment to self.__pin will not happen.
This ensures that only integer values can be set as a PIN.
len(str(new_pin)) == 4:

This converts new_pin to a string with str(new_pin) and checks if its length is 4.
This ensures that new_pin has exactly four digits.
For instance, if new_pin is 1234, str(new_pin) would be '1234', and len('1234') would be 4, so the condition would pass.
If new_pin has more or fewer than four digits (like 123 or 12345), this condition will fail, and 
the assignment will not occur.
self.__pin = new_pin:

If both conditions (new_pin is an integer and has exactly four digits) are True, this line assigns 
new_pin to the private attribute __pin.
This ensures that __pin is set only if new_pin meets both the integer type and 4-digit length requirements.
Purpose of the Validation
This validation ensures that only valid 4-digit integers (like a typical PIN code) are allowed to be assigned 
to __pin. If new_pin does not meet the conditions, the code does nothing, protecting __pin from invalid assignments."""

"""6. Write a class Student with a private attribute _grade. Use the setter method to ensure 
that the grade is between 0 and 100."""


class Student:
    def __init__(self, grade=0):
        self._grade = grade
        # Getter for grade (private attribute)

    def get_grade(self):
        return self._grade
    # Setter for grade (private attribute)

    def set_grade(self, grade):
        if isinstance(grade, int) and 0 <= grade <= 100:
            self._grade = grade
        else:
            print("Invalid grade. Please enter a number between 0 and 100.")


s1 = Student(25)
print(s1.get_grade())  # Output: 25
s1.set_grade(75)
print(s1.get_grade())

s1.set_grade(120)

"""7. Create a class Temperature with a private attribute _celsius. Implement getter and 
setter methods that convert between Celsius and Fahrenheit (e.g., set in Fahrenheit, store in Celsius). """
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
        # Getter for temperature in Celsius
    

"""8. Implement a BankAccount class with private attributes _account_number and 
_balance. Create methods to deposit and withdraw money, ensuring that the balance cannot become negative. """
class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number # Private attribute for account number
        self._balance = balance # Private attribute for balance
    
    