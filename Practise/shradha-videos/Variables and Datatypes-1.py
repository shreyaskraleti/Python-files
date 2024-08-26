print("Hello World")
print("my name is shreya")
print("my age is 30")
print("my name is shreya, my age is 30")
print(23)
print(30)
print(23+30)
print(23*2)

name = "shreya" # string - within double quotes or single quotes
age = 30
price = 25.03
print(name)
print(age)
print(price)

print("my name is:", name, "and",  "my age is :", age)

print(type(name))
print(type(age))
print(type(price))

print("name")
print('age')
print('''address''')

age = 25
print(type(age))

old = True
print(type(old))

a = 5.05
print(type(a))

x = "shreya"
print(type(x))

z = None
print(type(z))


a = 2
b = 5
sum = a+b
print(sum)

a = 5
b = 2
sub = a-b
print(sub)

# this is another recording
""" iam two'three
    five
    six """

# Operators:
# they will perform operation on operands
# 1. Arithmetic operators: +, -, *, /, %, **
a = 5
b = 2
print(a+b)  # output: 7
print(a-b)
print(a*b)
print(a/b)
print(a%b) # remainder
print(a**b)

# 2. Relational/comparison operators:
# ==, !=, >, <, >=, <=
a = 40
b = 50
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# 3. Assignment Operators:
# =, +=, -=, *=, /=, %=, **=
a = 10
b = 5
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a %= b
print(a)
a **= b
print(a)

# 4. Logical Operators:
# and, or , not
# and: both conditions must be true
# or: at least one condition must be true
# not: negates the condition
a = 10
b = 20
print(a>b and a<b)
print(a>b or a<b)
print(not (a>b))
print(not True)
print(not False)

# type conversion:
# int(), float(), str(), bool(), complex()
a = 10
print(int(a)) # converts to integer
print(float(a)) # converts to float
print(str(a)) # converts to string
print(bool(a)) # converts to boolean
print(complex(a)) # converts to complex number

b = 10.56
print(int(b))
print(float(b))
print(str(b))
print(bool(b))
print(complex(b))

# input:
# input() function is used to take input from the user
# it returns a string
# name = input("Enter your name: ")
# print("Welcome ", name)
# age = int(input("Enter your age: "))
# print("your age is ", age)
# salary = float(input("Enter your salary: "))
# print("your salary is", salary)

# program: 1. sum
a = int(input("enter first number: "))
b = int(input("Enter second number: "))
print("sum is :", a+b)

# 2. area
a = int(input("Enter your number: "))
print("area is :", a*a)

# 3. average
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
print("average is : ", (a+b)/2)

# 4. a >= b : True
# 5. a <= b : False
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a>=b)
print(a<=b)