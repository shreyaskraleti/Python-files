# map method:
#   - returns a new list with the results of applying the given function to each item of the original list.
#   - the function is applied to each item in the list, and the results are collected in a new list, which is then returned.
#   - the original list is not modified.
#  map() function in Python is a built-in function that applies a given function to all items of an iterable (such as a list, tuple, etc.)
# and returns a map object (which is an iterator).

#  The map() function takes two arguments: a function and an iterable. It applies the function
#  to each item in the iterable and returns a map object which is an iterator. The map
#  object is an iterator, meaning it is lazy and only computes the next value when asked for it.
#  The map() function is often used with lambda functions, which are small anonymous functions.
#  The map() function can be used with any type of iterable, including lists, tuples,
#  dictionaries, sets, etc.
#  The map() function returns a map object, which is an iterator. To get the results
#  as a list, you can use the list() function.

#  The map() function can be used with multiple iterables. In this case, the function
#  is applied to the corresponding items of each iterable. The map() function stops when
#  the shortest input iterable is exhausted.

# Syntax:
#   map(function, iterable, ....)

# example:
#   numbers = [1, 2, 3, 4, 5]
#   squares = list(map(lambda x: x**2, numbers))
#   print(squares)  # Output: [1, 4, 9,16,25]

# using lambda
a = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, a))
print(square)

cube = list(map(lambda x: x**3, a))
print(cube)

div = list(map(lambda x: x/2, a))
print(div)

# applying function to multiple iterables


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


a = [1, 2, 3]
b = [4, 5, 6]
add = list(map(add, a, b))
print(add)
sub = list(map(sub, a, b))
print(sub)

# applying function
a = [1, 2, 3]


def square(x):
    return x**2


squares = list(map(square, a))
print(squares)

# converting data types
string = ["1", "2", "3"]
integers = list(map(int, string))
print(integers)

# applying builtin functions using map:
numbers = [-1, -2, 3, -4, -5, 6, -7, 8, 9, -10]
absolute = list(map(abs, numbers))
print(absolute)
