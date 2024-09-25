# 1. Arithmetic operators:
# +, -, *, /, %, **, //, **
a = 10
b = 12
c = a+b
print(c)

a = 20
b = 12
c = a-b
print(c)

a = 20
b = 12
c = a*b
print(c)

d = 50
e = 20
f = d/e
print(f)

d = 50
e = 25
f = d%e
print(f)



d = 50
e = 20
f = d//e
print(f)

d = 5
e = 2
f = d**e
print(f)

#2. Comparison Operators
# ==, !=, >, <, >=, <=
a = 10
b = 12
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

a=10
b=12
if a>=b:
    print("a is greater or equal to b")
else:
    print("a is less than b")

a=5
b=2
if a<b:
    print("a is less than b")
else:
    print("a is greater than b")


#3. Assignment operators:
# =, +=, -=, *=, /=, %=, //=, **=
a = 10
b = 20
a = b
print(a)

a = 10
b = 20
a += b
print(a)

a = 20
b = 10
a -= b
print(a)

a = 20
b = 10
a *= b
print(a)

a = 20
b = 10
a /= b
print(a)

a = 20
b = 10
a %= b
print(a)

a = 20
b = 10
a //= b
print(a)

a = 2
b = 1
a **= b
print(a)

# 4. Logical Operators:
# and, or, not
a = 10
b = 20
print(a > b and a < b) # False
print(a > b or a < b) # True
print(not a > b) # True

a = 10
b = 5
print(a > b and a < b) # False
print(a > b or a < b) # True
print(not a > b) # False


# 5. Membership operators:
# in, not in
a = [10,12,25,30]
print(10 in a) # True
print(30 in a) # True
print(40 in a) # False
print(50 not in a)
print(70 not in a)
print(12 not in a)

#6. Identity operators:
# is, is not
a = 10
b = 10
print(a is b) # True
print(a is not b) # False
a = 20
b = 30
print(a is b) # False
print(a is not b) # True

#7. Ternary operators:
# condition if true : if false
a = 10
b = 20
print("A is greater than B") if a > b else print("B is greater than A")

a = 50
b = 70
print("a is less than b") if a < b else print("a is greater then b")


