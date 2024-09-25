# # # 1. Create a program that defines a global variable and a local variable 
# # with the same name. Use a function to print both the global and local 
# # variables. Explain the output. 
a = 20
print(f" a is a global variable {a}")
def var():
    a = 50
    print(f" a is a local variable {a}")
var()
    
# # 2. Write a function that modifies a global variable inside the function 
# using the global keyword. Demonstrate the effect by printing the 
# variable before and after the function call.

a = 10
print(a)
def varb():
    print(f" value of a before call of function is {a}")
def modify():
    global a
    a = 50
    print(f" value of a after call of function is {a}")
varb()
modify()

# # 3. Create a nested function where the inner function attempts to modify a 
# non-local variable. Use the nonlocal keyword to ensure the change 
# reflects in the outer function. Verify the output by printing the variable 
# before and after the inner function call.
def outer():
    x = 10
    print(f" value of x after call of outer function is {x}")
    def inner():
        nonlocal x
        x += 30
        print(f" value of x after call of inner function is {x}")
    inner()
outer()

# #4. Write a program that creates a counter using a global variable. The 
# program should have two functions: one to increment the counter and 
# one to decrement it. Verify that the global counter variable is updated 
# correctly after multiple function calls.
a = 10
def increment():
    global a
    a += 1
    print(f" value of a after increment is {a}")

def decrement():
    global a
    a -= 1
    print(f" value of a after decrement is {a}")
increment()
decrement()
decrement()

# # 5. Develop a program that defines a global list. Write two functions, one 
# to add elements to the list and another to remove elements. Use the 
# global keyword to modify the list within these functions. 
a = [1,2,3,4,5]
def add():
    global list
    a.extend([6,7,8])
    print(f" after adding elements the list is {a}")
def remove():
    global list
    a.remove(5)
    print(f" after removing elements the list is {a}")
add()
remove()

# # 6. Write a function that takes two numbers and returns their product. 
# Create an alias for this function and use it to calculate the product of 
# two other numbers. Compare the results of both function calls.
def mul(a,b):
    return a*b
prod_alias = mul
print(mul(5,6))
print(prod_alias(2,3))

# # 7. Define a function that returns the square of a number. Create an alias 
# for the function and demonstrate how both the original function and its 
# alias produce the same output for a given input.
def square(a):
    return a**2
sqr_alias = square
print(square(5))
print(sqr_alias(2))

# # 8. Write a lambda function to calculate the cube of a given number. Test 
# the lambda function with a list of numbers using the map function.
cube = lambda x: x**3
print(cube(3))
a = [1,2,3,4,5]
test = list(map(lambda x: x**3, a))
print(test)

# 9. Create a lambda function that filters out even numbers from a list. 
# Test it with a list of integers using the filter function. 
a = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x%2 == 0, a))
print(even)

# # 10.Write a lambda function to calculate the sum of two numbers. Use it 
# with the reduce function from the functools module to find the sum of 
# all elements in a list.
import functools
num = [12,13,42,21,15,67]
sum = functools.reduce(lambda a,b: a+b, num)
print(sum)

a = 10
b = 20
sum = functools.reduce(lambda a,b: a+b, [a,b])
print(sum)

# # 11.Create a list of numbers and use the map function to produce a new list 
# where each number is squared. Print both the original and the new list.
a = [1,2,3,4,5]
print(f" original list is {a}")
b = list(map(lambda x: x**2, a))
print(f" new list is {b}")

# # 12.Write a program that uses the filter function to filter out all the 
# negative numbers from a list. Test the program with a list that contains 
# both positive and negative integers.

a = [1,2,3,4,5,-1,-2,-3,-4,-5]
neg = list(filter(lambda x: x<0, a))
print(neg)

# # # 13.Write a function that calculates the factorial of a number using the 
# # reduce function. Test the function with a list of numbers.
# import functools
# def factorial(n):
#     return functools.reduce(lambda x: x*(x-1), n)
# factorial(5)


# # 14.Write a function that defines another function inside it. The inner 
# function should take a number as an argument and return its square. 
# The outer function should return the inner function and demonstrate 
# its usage.
def outer():
    def inner(x):
        return x**2
    return inner
res = outer()
print(res(5))

# # 15.Create a nested function where the outer function calculates the sum of 
# two numbers, and the inner function calculates the product of the same 
# two numbers. Return both results as a tuple. Test the function with 
# different pairs of numbers.


def outer(a, b):
    sum = a+b
    def inner():
        return a*b
    return sum, inner()


res1 = outer(5, 3)

res2 = outer(6, 3)

res3 = outer(7, 3)

print(res1)
print(res2)
print(res3)

