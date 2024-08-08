# 1. using predefined function:
import numpy as np
A = np.array([[1,2,3],
              [4,5,6]])
AT = np.transpose(A)
print(A)
print(AT) # rows changed to columns in transpose

# 2. case2:
A = np.array([[1,2,3],
              [4,5,6]])
AT = A.T # transpose the matrix
print(A)
print(AT)

# String functions:
# modulename.char.functionname
# numpy.char.functionname
# np.char.add()
# np.char.lower()
# np.char.upper()

arr1 = np.array(['apple', 'banana', 'cherry'])
arr2 = np.array([' is red', ' is yellow', ' is cherry-red'])
result = np.char.add( arr1, arr2)
print(result)

arr1 = np.array(['rose', 'lily'])
arr2 = np.array([' is red', ' is white'])
result = np.char.add(arr1,arr2)
print(result)

arr1 = np.array(['Apple', 'Banana', 'Cherry'])
result = np.char.lower(arr1)
print(result)

arr1 = np.array(['Apple', 'Banana', 'Cherry'])
result = np.char.upper(arr1)
print(result)

# Strip - head and tails
arr1 = np.array([' Hello  ' , '  Phani  '])
result = np.char.strip(arr1)
print(result)

# replace:
arr1 = np.array(['hello', 'phani'])
result = np.char.replace(arr1, 'phani', 'bonky')
print(result)

arr1 = np.array(['hello', 'shreya'])
result = np.char.replace(arr1, 'shreya', 'bonky')
print(result)

# split():
a = "shreya likes bonky"
b = a.split()
print(b)

c = "shreya is studying at achieversit"
d = np.char.split(c,'s')
e = np.char.split(c, 'a')
print(d)
print(e)

# join():
arr1 = np.array(['hello', 'shreya'])
result = ''.join(arr1)
print(result)

arr2 = np.array(['hello', 'world'])
result = ''.join(arr2)
print(result)

# shape:
arr1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr1.shape)

# dtype:
arr1 = np.array([[1,2,3],
                 [4,5,6]])
print(arr1.dtype)

# find:
arr1 = np.array(['hello', 'world'])
result = np.char.find(arr1, 'world') # in first element world is not available so result is -1 and second element world is available and start index is 0, so result is 0.
print(result)

arr1 = np.array(['hello', 'world', 'noudurishreya'])
result = np.char.find(arr1, 'shreya')
print(result)

# endswith - True or False
arr1 = np.array(['hello', 'shreya'])
result = np.char.endswith(arr1, 'a')
print(result)

# startswith:
arr1 = np.array(['hello', 'shreya'])
result = np.char.startswith(arr1, 's')
print(result)

arr1 = np.array(['hello', 'shreya'])
result = np.char.startswith(arr1, 'h')
print(result)

# using arithmetic operator:
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
result = arr1 * arr2
print(result)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
result = arr1 + arr2
print(result)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
result = arr1 - arr2
print(result)

arr1 = np.array([12, 21, 24, 18, 50])
arr2 = np.array([6, 7, 8, 9, 10])
result = arr1 / arr2
print(result)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 2, 3, 3])
result = arr1 ** arr2
print(result)

arr1 = np.array([12, 21, 24, 18, 50])
arr2 = np.array([6, 7, 8, 9, 10])
result = arr1 % arr2
print(result)

# using logical operators:

a = np.array([True, False, True])
b = np.array([True, True, False])
result = a & b
print(result)

a = np.array([True, False, True])
b = np.array([True, True, False])
result = np.logical_and(a,b)
print(result)

a = np.array([True, False, True])
b = np.array([True, False, False])
result = a | b
print(result)

a = np.array([True, False, True])
b = np.array([True, False, False])
result = np.logical_or(a,b)
print(result)

a = np.array([True, False, True])
result = ~a
print(result)

a = np.array([True, False, True])
result = np.logical_not(a)
print(result)

a = np.array([True, False, True, False])
b = np.array([False, True, True, False]) # xor gives output as false when both are true and when both are false.
result = np.logical_xor(a,b)
print(result)

# Relational operator:
# np.greater() function is used to compare two arrays element-wise and return a new array where the elements are the result of the comparison.
# np.less():
# np.greater_equal():
# np.less_equal():
# np.not_equal():
# np.equal():
arr1 = np.array([21,50])
arr2 = np.array([10,12])
result = np.greater(arr1,arr2)
print(result)

arr1 = np.array([21,50])
arr2 = np.array([10,12])
result = np.less(arr1,arr2)
print(result)

arr1 = np.array([10,12])
arr2 = np.array([10,12])
result = np.equal(arr1,arr2)
print(result)

arr1 = np.array([21,50])
arr2 = np.array([10,12])
result = np.not_equal(arr1,arr2)
print(result)

arr1 = np.array([21,50])
arr2 = np.array([10,12])
result = np.greater_equal(arr1,arr2)
print(result)

arr1 = np.array([10,12])
arr2 = np.array([10,12])
result = np.less_equal(arr1,arr2)
print(result)

arr1 = np.array([10,12])
arr2 = np.array([10,12])
result = arr1 > arr2
print(result)

arr1 = np.array([10,12])
arr2 = np.array([10,12])
result = arr1 < arr2
print(result)

arr1 = np.array([10,12])
arr2 = np.array([10,12])
result = arr1 == arr2
print(result)

arr1 = np.array([10,12])
arr2 = np.array([10,12])
result = arr1 >= arr2
print(result)

arr1 = np.array([10,12])
arr2 = np.array([10,12])
result = arr1 <= arr2
print(result)

arr1 = np.array([100,12])
arr2 = np.array([10,120])
result = arr1 != arr2
print(result)










