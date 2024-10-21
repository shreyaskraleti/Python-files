# 1. Write a program that swaps two numbers a = 15 and b = 27 using bitwise XOR.
"""Here’s how the bitwise XOR swap works step-by-step with an example, starting with a = 15 and b = 27:
Binary Representation:
a = 15 → Binary: 0000 1111
b = 27 → Binary: 0001 1011
Step-by-Step Execution:
First XOR operation:

css
Copy code
a = a ^ b
a = 15 ^ 27
a = (0000 1111) ^ (0001 1011) = 0001 0100
Now, a = 20 (in decimal), and b = 27.

Second XOR operation:

css
Copy code
b = a ^ b
b = 20 ^ 27
b = (0001 0100) ^ (0001 1011) = 0000 1111
Now, b = 15 (original value of a), and a = 20.

Third XOR operation:

css
Copy code
a = a ^ b
a = 20 ^ 15
a = (0001 0100) ^ (0000 1111) = 0001 1011
Now, a = 27 (original value of b).

Final Result:
After the three XOR operations, the values are swapped:
a = 27
b = 15
No temporary variable was used, and the swap was done using only XOR operations!"""

a = 15
b = 27
# Use the XOR operator (^) to swap the values of a and b.
a = a ^ b
b = a ^ b
# Now, a = a ^ b will give the original value of b.
a = a ^ b
print("after swapping two numbers a is: ", a, " and b is: ", b)