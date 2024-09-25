""" Identifier:
An identifier is a name used to identify a variable, function, class, module, or any other object in a program. In Python, an identifier is a user-defined name that follows certain rules:
It can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
It cannot start with a digit.
It cannot use reserved keywords like if, else, while, etc.
It is case-sensitive (myVar and myvar are different identifiers). """

# 1. Create three different identifiers for variables and assign them the values 10, 20, and 30. Print the values of these variables. 
a = 10
b = 20
c = 30
print(a)
print(b)
print(c)

# 2. Write a program that tries to use an identifier starting with a number and observe the error message. Explain why the error occurred.
""" 
1a = 20
print(1a)
SyntaxError: invalid decimal literal
This will raise a SyntaxError because Python does not allow identifiers to start with a digit.
The error occurred because Python does not allow identifiers to start with a digit. This is a
fundamental rule in Python's syntax. Identifiers are used to name variables, functions, classes,
etc., and Python needs to be able to distinguish them from numbers. If an identifier starts with
a digit, it would be ambiguous and could lead to errors. """
 
# 3. List 10 reserved keywords in Python and explain why they can't be used as identifiers.
""" 10 reserved keywords in python are:
1. False
2. True
3. None
4. if
5. else
6. While 
7. for
8. return
9. Def
10. Class
11. print
Reserved keywords in Python have predefined meanings and functions. 
These words are part of the core syntax of the language, and using them as identifiers would cause confusion in the interpreter, 
as it would not be able to distinguish between your intended variable name and the language's built-in commands.
For example:
Using if as a variable name would clash with its role in conditional statements.
Using def would conflict with defining a function. """

# 4. Write a program using at least five different reserved keywords correctly. 
def greet(name):
    if name == "shreya":
        return "Hello, " + name
    else:
        return "Hello stranger!"
print(greet("shreya"))

# 5. Declare two variables, name and age, and assign them your name and age. Print a sentence that uses both variables.
name = "shreya"
age = 30
print(f" my name is {name} and age is {age}")

# 6. Define a constant PI with the value 3.14159. Use comment to explain about it. 
"""In Python, constants are typically written in uppercase to signify that their values should not change during the program's execution. However, Python does not enforce this, so it's just a convention."""
PI = 3.14159
# PI is a mathematical constant representing the ratio of a circle's circumference to its diameter.

# 7. Write a Python program with a simple if-else condition that prints "Even" if a number is even and "Odd" if it is odd. Ensure the program is properly indented.
def even(num):
    if num % 2 == 0:
        return "Even"
    else:
        
        return "Odd"
print(even(5))

# 8. Write a Python program that includes at least three comments explaining what different parts of the code do. 
# The comments explain the purpose of the function and the conditional logic used to generate different greeting messages.
def greet(name):
    # This function takes a name as input and returns a greeting message
    if name == "shreya":
        # If the name is "shreya", return a personalized greeting message
        return "Hello, " + name
    else:
        # If the name is not "shreya", return a generic greeting message
        return "Hello stranger!"
print(greet("shreya")) # calling the greet function with name shreya

# 9. Create a multi-line comment that describes the purpose of a program that calculates the area and perimeter of a rectangle.
""" This program calculates the area and perimeter of a rectangle.
It takes the length and width of the rectangle as input from the user and uses the following formulas:
- Area = length * width
- Perimeter = 2 * (length + width)
The program then outputs the calculated area and perimeter. """
def rectangle(l,w):
    area = l * w
    perimeter = 2 * (l+w)
    return area, perimeter
print(rectangle(2,5))

""" 10. Define a variable named favorite_color and assign it your favorite color. 
Write a comment explaining why you chose that color and how comments are useful in code."""
favorite_color = "blue"
""" I like blue color a lot, so i have chosed this color. comments are useful to explain the logic and functionality of the code."""


