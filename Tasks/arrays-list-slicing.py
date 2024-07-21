# docstring: 
def add(a,b):
    """ add two numbers and return the result """
    return (a+b)

print(add.__doc__)
print(add(3,5))

def sub(a,b):
    """
        subtract two numbers and return the result
    
    """
    return(a-b)
print(sub.__doc__)
print(sub(8,2))

import math
result = math.sqrt(25)
print(result)

import math
result = math.sin(30)
print(result)

# Slicing: 
# Slicing is a way to extract a subset of a sequence.
# Slicing is done by specifying the start and end index of the subset.
# The start index is inclusive, and the end index is exclusive.
# [start:stop:skip]

l = [2,3,4,5,6]
print(l[3])
print(l[-1])
print(l[0:3])

# array:
# An array is a data structure that stores a collection of values.
# The values in an array are stored in a contiguous block of memory.
# This means that the values in an array are stored in a specific order,
# and can be accessed by their index.
# The index of the first element in an array is 0, and the index of the last
# element is the length of the array minus 1.
# The length of an array can be obtained by using the len() function.

import array
a = array.array('i', [2,3,4,5,6,7])
print(a)

import array
a = array.array('f', [1.05, 2.03, 4.0888])
print(a)
print(type(a))
print(a.append(12.35))
print(a)
print(a.insert(3, 23.567))
print(a)

import array
a = array.array('i', [1,2,3,4,5,6])
print(a)
print(type(a))
print(a.index(1))
print(a.index(4))
print(a.append(13))
print(a)
print(a.insert(2,15))
print(a)
print(a.pop(2))
print(a)
print(a.extend([1,2,3,4]))
print(a)
print(a.remove(5))
print(a)
print(a.reverse())
print(a)

# list:
# A list is a data structure that stores a collection of values.
# The values in a list are stored in a contiguous block of memory.
# This means that the values in a list are stored in a specific order,and can be accessed by their index.
# The index of the first element in a list is 0, and the index of the last element is the length of the list minus 1.
# The length of a list can be obtained by using the len() function.
# A list can contain values of different types, and can be modified.
# A list can be created by using the list() function.
# allows duplication of data
# mutable

a = [1,2,3,4,5,6]
print(a[-1])
print(a[0:3])
print(type(a))
print(a[0:5:2])
print(a[::1])
print(a[::-1])

b = ["shreya", "bonky", 2,3,4,5,2,3,4,2,3]
print(b)
print(type(b))
print(b[-1])
b[0] = 23
print(b)
print(len(b))