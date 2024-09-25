# control statements:
# 1. if
# 2. if-else
# 3. elif
# 4. nested if

# if 
a = 10
b = 20
if a<b:
    print("a is less than b")
    
# if-else
a = 28
b = 20
if a<b:
    print("a is less than b")
else:
    print("a is greater than b")
    
# elif 
a = 30
b = 20
if a<b:
    print("a is less than b")
elif a!=b:
    print("elif block 1")
elif a==b:
    print("elif block 2")
else:
    print("a is greater than b")
    
# nested-if
a = 10
b = 20
if a<b:
    print("a is ready to enter inner loop")
    if a==b:
        print("inner loop executes")
    else:
        print("inner loop fails")
else:
    print("outer loop fails")
    
# conditional statements:
# for loop
fruits = ['pineapple', 'kiwi', 'grapes']
for i in fruits:
    print(i)

for i in range(1,10):
    print(i)
    
for i in range(20):
    print(i)
    
# while loop
i = 1
while i < 10:
    print(i)
    i = i + 1
    
a = 2
while a < 8:
    print(a)
    a = a + 1
    
# Jump statements:
# break, continue, pass, lambda

# lambda
add = lambda a,b : a+b
print(add(3,5))

mul = lambda x,y : x*y
print(mul(2,3))

div = lambda d,e : d/e
print(div(4,2))

# pass
class Example:
    pass

class Fruits:
    pass


# for-break and continue
for i in range(1,10):
    if i==7:
        break
    print(i)

# continue
for i in range(1,10):
    if i==5:
        continue
    print(i)
    
# while-break and continue
i = 1
while i < 10:
    if i==7:
        break
    print(i)
    i = i + 1
    
i = 1
while i < 10:
    if i==5:
        continue
    print(i)
    i = i + 1
    



    
    


  

