# list comprehension:
#   - faster than for loop
#   - more memory efficient than for loop
#   - more readable than for loop
#   - more concise than for loop
#   - can be used with if condition to filter out elements
#   - can be used with multiple lists to create a new list with elements from all lists
#   - can be used with functions to apply a function to each element in the list
#   - can be used with if-else condition to create a new list with elements based on
#     a condition
#   - can be used with enumerate to get both index and value of each element in the list
#   - can be used with zip to create a new list with elements from multiple lists
#   - can be used with map to apply a function to each element in the list
#   - can be used with filter to filter out elements based on a condition
#   - can be used with lambda function to create a new list with elements based on a condition
#   - can be used with sorted to sort the list in ascending or descending order
#   - can be used with reversed to reverse the list
#   - can be used with any function that takes an iterable as an argument

# basic list comprehension:
#   - syntax: [expression for variable in iterable]
square = [x**2 for x in range(10)]
print(square)

cube = [x**3 for x in range(10)]
print(cube)

# list comprehension with condition:
#   - syntax: [expression for variable in iterable if condition]
even = [x for x in range(10) if x%2==0]
print(even)

odd = [x for x in range(10) if x%2!=0]
print(odd)

# set comprehension:
#   - syntax: {expression for variable in iterable}
#   - creates a set with unique elements

x = {x for x in range(20)}
print(x)
x = {x for x in range(10)}
print(x)

#   - creates a set with unique elements based on a condition
# {expression for item in iterable if condition}

x = {x**2 for x in range(10) if x%2==0}
print(x)
x = {x for x in range(20) if x%2!=0}
print(x)

# dictionary comprehension:
#   - syntax: {key: value for variable in iterable}
#   - creates a dictionary with key-value pairs
#   - key and value can be any type of object
#   - key must be unique
#   - value can be any type of object

square = {x:x**2 for x in range(10)}
print(square)

cube = {x:x**3 for x in range(10)}
print(cube)

# {key_expression: value_expression for item in iterable if condition}

even = {x:x**2 for x in range(10) if x%2==0}
print(even)

odd = {x:x**3 for x in range(10) if x%2!=0}
print(odd)

