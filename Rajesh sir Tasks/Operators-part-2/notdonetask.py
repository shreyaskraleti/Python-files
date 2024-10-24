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

# 2. Perform bitwise NOT operation on a number n = 25. What is the result?
"""The bitwise NOT operation inverts the bits of a number. For a number 
𝑛=25
n=25:
In binary, 25 is represented as:
25=00011001
25=00011001
Performing a bitwise NOT on this results in:
NOT 25=11100110
NOT 25=11100110
In two's complement representation (used for negative numbers in computers), this binary value corresponds to 
−26
−26.

Thus, the result of the bitwise NOT operation on 25 is:
Result=−26
Result=−26"""

n = 25
result = ~n
print(result)

# 3. Write a program that checks if a given number n = 16 is a power of 2 using bitwise operators.
"""Here's an explanation of the code:

Function Definition:

is_power_of_two(n) checks if a number n is a power of 2 using bitwise operations.
Condition (n & (n - 1)) == 0:

In binary, powers of 2 have only one bit set to 1 (e.g., 1 = 0001, 2 = 0010, 4 = 0100, etc.).
Subtracting 1 from a power of 2 flips all the bits after the rightmost 1 bit. For example:
16 in binary is 10000.
16 - 1 = 15, which in binary is 01111.
Performing a bitwise AND (&) on 16 and 15 gives 00000, which is 0.
This works only for powers of 2 because for other numbers, the result of n & (n - 1) will not be zero.
Return Statement:

The expression checks two conditions:
n > 0: Ensures the number is positive.
(n & (n - 1)) == 0: Ensures it's a power of 2.
If both are true, the function returns True.
Main Program:

The program calls is_power_of_two(n) with n = 16.
If the function returns True, it prints that the number is a power of 2. Otherwise, it prints that it is not."""

def power(n):
    return n > 0 and (n & (n-1)) == 0
n = 16
if power(n):
    print(f" {n} is a power of 2")
else:
    print(f" {n} is not a power of 2")
