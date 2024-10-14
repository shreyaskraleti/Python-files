# 1. Write a Python program that takes a string input from the user and converts it to an integer.
# Print the integer and its type.
a = input("enter a number:")
print(type(a))
print(int(a))
print(type(int(a)))

# 2. Write a Python program that converts a floating-point number to an integer. 
# Print both the original float and the converted integer. 
a = float(input("enter a number:"))
print(type(a))
print(int(a))
print(type(int(a)))

# 3. Write a Python program that takes an integer input from the user and converts it to a string. 
# Print the string and its type. 
a = int(input("enter a number:"))
print(type(a))
print(str(a))
print(type(str(a)))

# 4. Write a Python program that converts a string representing a number with decimals to a float. 
# Print the original string and the converted float. 
a = "25.56"
print(type(a))
print(float(a))
print(type(float(a)))

# 5. Write a Python program that takes a boolean value and converts it to an integer.
# Print both the original boolean value and the converted integer.
a = True
print("original boolean value", a)
print(type(a))
b = int(a)
print("converted integer value is ", b)
print(type(b))

# 6. Write a Python program that takes an integer input from the user and converts it to a boolean. 
# Print both the original integer and the converted boolean.
s = int(input("enter a number: "))
print("integer value is ", s)
print(type(s))
h = bool(s)
print("boolean value is ", h)
print(type(h))

# 7. Write a Python program that takes a list of strings representing numbers and converts each string to an integer. 
# Print the original list and the list of integers.
"""The current code will raise an error because int() cannot be directly applied to a list. You need to convert each element in the list individually. Here’s how you can modify the program:
python. This uses a list comprehension to convert each string in the list to an integer, and then prints both the original and converted lists.
In this output: The original list contains strings. The converted list contains integers."""
d = ["1", "2", "3", "4", "5"]
print("original list is ", d)
print(type(d))
e = [int(i) for i in d]
print("list of integers is ", e)
print(type(e))

# 8. Write a Python program that takes a tuple of floating-point numbers and converts each float to an integer. 
# Print both the original tuple and the new tuple with integers.
""" The current code will raise an error because int() cannot be directly applied to a tuple. You
need to convert each element in the tuple individually. Here’s how you can modify the program: """
f = (1.2, 2.5, 4.6, 6.7, 9.0, 10.2)
print("original tuple is: ", f)
print(type(f))
g = tuple(int(i) for i in f)
print("tuple with integers is: ", g)
print(type(g))

# 9. Write a Python program that converts a complex number to a string and prints both the 
# original complex number and the converted string.
a = 3 + 2j
print("complex number is :", a)
print(type(a))
b = str(a)
print("converted string is: ", b)
print(type(b))

# 10. Write a Python program that takes a string representing a complex number 
# (e.g., '3+4j') and converts it to a complex number. 
# Print the original string and the converted complex number.
c = input("enter a complex number: ")
print("original string is :", c)
print(type(c))
d = complex(c)
print("converted complex number is :", d)
print(type(d))

# 11. Write a Python program that converts an integer to bytes and prints both 
# the original integer and the converted bytes.
"""To convert an integer into a byte representation, you should use the int.to_bytes() method, specifying the number of bytes and the byte order (big-endian or little-endian).
xplanation:
a.to_bytes(2, byteorder='big'):
2 specifies that we want to use 2 bytes to represent the integer.
byteorder='big' indicates that the most significant byte is at the beginning (big-endian format).
This will convert the integer 20 into its corresponding byte representation.
Here, the integer 20 is converted into a 2-byte representation b'\x00\x14', where \x00 is the padding byte, and \x14 is the hexadecimal representation of 20."""
a = 20
print("original integer is :", a)
print(type(a))
b = a.to_bytes(3, byteorder='big')
print("converted bytes is: ", b)
print(type(b)) # padding byte is placed first
a = 20
print("original integer is :", a)
print(type(a))
b = a.to_bytes(2, byteorder='little')
print("converted bytes is: ", b)
print(type(b)) ## hexadecimal is placed first

# 12. Write a Python program that takes a bytes object and converts it to a string. 
# Print both the original bytes object and the converted string. 
"""decode('utf-8'): This method converts the bytes object into a string, specifying the UTF-8 encoding. UTF-8 is a common text encoding that works for most cases."""
bytes_object = b'hello phani !'
print("original bytes object is:", bytes_object)
print(type(bytes_object))
converted_string = bytes_object.decode('utf-8')
print("converted string is:", converted_string)
print(type(converted_string))

# 13. Write a Python program that takes a list of integers and converts each integer to a string. 
# Print the original list and the list of strings.
a = [1,2,3,4,5]
print("original integer list is: ", a)
print(type(a))
b = [str(i) for i in a]
print("list of strings is :", b)
print(type(b))

# 14. Write a Python program that takes a string input from the user and converts it to a boolean. 
# Print both the original string and the converted boolean.
"""Any non-empty string is True.
An empty string ("") is False."""
a = input("enter a string:")
print("original string is :", a)
print(type(a))
b = bool(a)
print("converted boolean is :", b)
print(type(b))

# 15. Write a Python program that takes a string input from the user and converts it to a list of individual characters. 
# Print both the original string and the list of characters.
a = input("enter a string:")
print("original string is:", a)
print(type(a))
b = list(a)
print("list of characters is:", b)
print(type(b))