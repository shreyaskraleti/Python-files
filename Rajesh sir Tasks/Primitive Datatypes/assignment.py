# Integer Assignments 
# 1. Add the integers 5 and 10. What is the result? 
add = 5 + 10
print(add)
# 2. Subtract 7 from 15. What is the result? 
sub = 15 - 7
print(sub)
# 3. Multiply 3 by 4. What is the result? 
mul = 3 * 4
print(mul)
# 4. Divide 20 by 4. What is the result?
div = 20 / 4
print(div)

# Float Assignments 
# 5. Add the floats 5.5 and 10.2. What is the result? 
add = 5.5 + 10.2
print(add)
# 6. Subtract 7.1 from 15.3. What is the result? 
sub = 15.3 - 7.1
print(sub)
# 7. Multiply 3.6 by 4.5. What is the result? 
mul = 3.6 * 4.5
print(mul)
# 8. Divide 20.8 by 4.2. What is the result? 
div = 20.8 / 4.2
print(div)

# Complex Number Assignments 
# 9. Add the complex numbers 3 + 4j and 1 + 2j. What is the result? 
add = (3+4j)  +  (1+2j)
print(add)
# 10. Subtract the complex number 2 + 3j from 5 + 6j. What is the result?
sub = (5+6j) - (2+3j)
print(sub)

# Boolean Assignments 
# 11. Compare if 5 is greater than 10. What is the result? 
if 5 > 10:
    print(True)
else:
    print(False)
# 12. Perform a logical AND operation on True and False. What is the result? 
res = True and False
print(res)

# None Assignments 
# 13. Check if a variable set to None is equal to None. What is the result? 
a = None
res = (a == None)
print(res)

# Bytes and Bytearray Assignments 
# 14. Create a bytes object from the list [1, 2, 3, 4, 5]. What does the bytes object look like? 
byte_object = bytes([1, 2, 3, 4, 5])
print(byte_object)

"""A byte object in Python is an immutable sequence of bytes, where each byte is an 8-bit value (ranging from 0 to 255). 
It is commonly used for handling binary data, such as files, network data, or text encoded in formats like UTF-8.

Key features of a bytes object:
It is similar to a string, but instead of characters, it holds raw byte values.
You can't modify a bytes object after it's created (immutable).
It is prefixed with a b, like b"""

# 15. Create a bytearray from the list [1, 2, 3, 4, 5] and modify the first element to 10. 
# What does the bytearray look like? 
"""A bytearray in Python is a mutable sequence of bytes, similar to a bytes object, 
but with the key difference that you can modify its elements after creation.

Key features of bytearray:
It holds byte values ranging from 0 to 255.
It is mutable, so you can change its contents (e.g., add, remove, or modify elements).
It is often used for binary data manipulation, 
such as when working with files or streams that require changes to individual bytes."""
byte_array = bytearray([1, 2, 3, 4, 5])
byte_array[0] = 10
print(byte_array)

# Give an example for these bytearray methods: 
# append(),extend(), insert(), remove(), 
# pop(), clear(), reverse(), copy(), count(), 
# index(), find(), join(), split(), replace(), decode()
# append():
ba = bytearray([1,2,3])
ba.append(4)
print(ba)
# extend():
ba = bytearray([1,2,3])
ba.extend([4,5,6])
print(ba)
# insert():
ba = bytearray([1,2,3])
ba.insert(2,5)
print(ba)
# remove():
ba = bytearray([1,2,3,4,5])
ba.remove(3)
print(ba)
# pop():
ba = bytearray([1,2,3,4,5])
ba.pop(3)
print(ba)
# clear():
ba = bytearray([1,2,3,4,5])
ba.clear()
print(ba)
# reverse():
ba = bytearray([1,2,3,4,5])
ba.reverse()
print(ba)
# copy():
ba = bytearray([1,2,3,4,5])
bc = ba.copy()
print(bc)
# count():
ba = bytearray([1,2,2,3,4,4,5])
print(ba.count(2))
print(ba.count(4))
#  index():
ba = bytearray([1,2,3,4,5])
print(ba.index(3))
#  find():
ba = bytearray([1,2,3,4,5])
print(ba.find(4))
