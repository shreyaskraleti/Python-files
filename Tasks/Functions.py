# Ennumerate Function - will provide index for the data
# enumerate() function returns an enumerate object. It contains the index and the value, as a pair
# enumerate() function takes a list as an argument and returns an enumerate object. The enumerate object yields

fruits = ["apple", "pineapple", "grapes"]
print(type(fruits))
for index, fruit in enumerate(fruits):
    print("Index:", index, "fruits:", fruit)
    
chocolates = ["dairymilk", "munch", "perk"]
print(type(chocolates))
for index, choco in enumerate(chocolates):
    print("Index:", index, "chocolates:", choco)

# using zip:
# zip() function used to combine 2 data
# zip() function combines multiple iterables element wise.
# zip() function returns an iterator of tuples based on the iterable objects.

name = ["shreya", "phani", "bonky"]
age = [30, 32, 2]
for n,a in zip(name, age):
    print("name:", n, "age:", a)

fname = ["shreya", "phani", "bonky"]
lname = ["kraleti", "nouduri", "deepusubbu"]
for f,l in zip(fname, lname):
    print("first name:", f, "last name:", l)
    
# Iteration through for loop:
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable

name = ["shreya", "phani", "bonky"]
for names in name:
    print(name)
    
age = [30, 32, 2]
for ages in age:
    print(age)
    
# .format():
# .format() method is used to format the string. It is used to insert the value of
# a variable inside a string.
a = 20
b = 30 
c = a+b
print("a is {} b is {} and their sum is {}".format(a,b,c))

a = 6
b = 2
c = a*b
print("multiplying a is {} and b is {} result is c {}".format(a,b,c))
    
# Function:
# A function is a block of code which only runs when it is called. You can pass data
# , known as parameters, into a function. A function can return data as a result.

# basic function:
def myfunction():
    print("Hello World")
myfunction()

#function with default parameters:
def add(a,b):
    return a+b
print(add(2,3))

def mul(a,b):
    return a*b
print(mul(3,5))

# types of default arguments:
# a,b
# a=2,b=3
# a, b=3
# a=2, b

def add(a,b):
    return a+b
print(add(2,3))

def add(a=2,b=3):
    return a+b
print(add(5,6))

def add(a, b=3):
    return a+b
print(add(2,8))

# def add(a=2, b): # this doesnt work - non default parameter following parameter with default
  #  return a+b
# print(add(3,1))

# function with variable-length argument:
def add(*args):
    return sum(args)
print(add(1,2,3,4,5,6,7,8,9))

def x(*args):
    return args
print(x(1,2,3,4,5,6,7,8,9))

def multiply(x,y):
    return x*y
print(multiply(2,3))

x = [1,2,3,4,5,6]
print(len(x))
print(min(x))
print(max(x))