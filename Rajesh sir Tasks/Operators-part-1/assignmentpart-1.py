# 1. Explain what arithmetic operators are in Python and list all the arithmetic operators with examples.
"""Arithmetic operators in Python are symbols used to perform mathematical operations on numeric data. 
Here's a list of all the arithmetic operators with examples:

Addition (+)
Adds two values.
add = 5 + 3 
Subtraction (-)
Subtracts the right-hand operand from the left-hand operand.
sub = 5 - 3
Multiplication (*)
Multiplies two values.
mul = 5 * 3
Division (/)
Divides the left-hand operand by the right-hand operand (floating-point division).
div = 5 / 3
Floor Division (//)
Divides and returns the largest integer smaller than or equal to the result (also called integer division).
floor_div = 5 / 3
Modulus (%)
Returns the remainder of dividing the left-hand operand by the right-hand operand.
mod = 5 / 3
Exponentiation ()**
Raises the left-hand operand to the power of the right-hand operand.
pow = 2 ** 3
"""

# 2. Define relational operators in Python. Why are they also called comparison operators? List them with examples. 
""" Relational operators in Python, also known as comparison operators, are used to compare two values and determine the relationship between them. 
They are called comparison operators because they compare operands and return a Boolean value (True or False).

Here’s a list of the relational operators with examples:
Equal to (==)
Checks if two values are equal.
res = (2 == 2)
Not equal to (!=)
Checks if two values are not equal.
res = (3 != 2)
Greater than (>)
Checks if the left operand is greater than the right operand.
res = (7 > 2)
Less than (<)
Checks if the left operand is less than the right operand.
res = (5 < 10)
Greater than or equal to (>=)
Checks if the left operand is greater than or equal to the right operand.
res = (10>=4)
Less than or equal to (<=)
Checks if the left operand is less than or equal to the right operand.
res = (5<=5)
"""

# 3. What are logical operators in Python? List the three logical operators and describe their function with examples. 
"""Logical operators in Python are used to combine multiple conditions or expressions, returning a 
Boolean value (True or False) based on the logic applied.
Here are the three logical operators:

AND (and)
Returns True if both conditions are True.
res = (5>3 and 7<10)
OR (or)
Returns True if at least one of the conditions is True.
res = (5>3 and 10>20)
NOT (not)
Reverses the Boolean value of the condition. Returns True if the condition is False, and vice versa.
result = not(5>3)
"""

# 4. Explain the purpose of assignment operators in Python. How do they differ from relational operators? 
"""Assignment operators in Python are used to assign values to variables. 
They not only store a value but can also perform operations like addition, subtraction, etc., during the assignment.
Difference from Relational Operators:
Assignment operators assign a value to a variable, 
while relational operators compare values and return a Boolean result (True or False).
List of Assignment Operators:
= (Simple assignment)
Assigns a value to a variable.
x = 5
+= (Addition assignment)
Adds a value to the variable and reassigns the result.
x += 3
-= (Subtraction assignment)
Subtracts a value from the variable and reassigns the result.
x -= 2
*= (Multiplication assignment)
Multiplies the variable by a value and reassigns the result.
x *= 4
/= (Division assignment)
Divides the variable by a value and reassigns the result.
x /= 10
//= (Floor division assignment)
Performs floor division and reassigns the result.
x //= 2
%= (Modulus assignment)
Finds the remainder and reassigns the result.
x %= 2
**= (Exponentiation assignment)
Raises the variable to a power and reassigns the result.
x **= 3
"""

# 5. Write a Python program to perform the following arithmetic operations on two numbers: addition, subtraction, multiplication, division, and 
# modulus.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
floor_division = a//b
print("Addition is ", addition)
print("Subtraction is ", subtraction)
print("Multiplication is ", multiplication)
print("Division is ", division) # output in float
print("Floor division is ", floor_division) # output in integer
print("Modulus is ", modulus)

# 6. Write a Python program that compares two numbers and prints whether 
# the first number is greater than, less than, or equal to the second number.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("a is equal to b")

# 7. Write a Python program where you start with a variable x = 10 and then 
# perform the following operations sequentially: += 5, -= 2, *= 3, and /= 4. Print the result after each operation.
x = int(input("enter a number:"))
x += 5
print("after adding with 5, x is ", x)
x -= 2
print("after subtracting with 2, x is ", x)
x *= 3
print("after multiplying with 3, x is ", x)
x /= 4
print("after dividing with 4, x is ", x)

# 8. Write a Python program that takes two boolean variables, A and B, and print the result of A and B, A or B, and not A.
A = True
B = False
print(A and B)
print(A or B)
print(not A)
print(not B)