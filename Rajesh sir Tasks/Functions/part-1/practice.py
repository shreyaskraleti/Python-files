# #block of code, encapsulation , takes ip and give us output
# #synatx : def function_name(): block of code function_name()

# def greet():
#     print("hi")

# greet()

# #parameter,arguments
# def f1(name,age):
#     print(f"hi im {name} and {age}")
#     print("Hi iam", name ,"my age is", age)
# f1("Bonkers",1)

# #return statement: retun the value,terminates the code after return
# def f2(x,y):
#     return x+y
#     print("Hi")
# print(f2(5,6))
#res = f2(10,10)
# #print(res)

# #return statement can return more than 1 object or value,in python
# def add_sub(a,b):
#     add = a+b
#     sub = a-b
#     mult = a%b
#     return add,sub,mult
# x,y,z = add_sub(30,20)
# print(x,y,z)

#Types of argument: positional,keyword,default, variable length aribitary- *args, **kwargs

def pos(name,age):
    print(f"hi im {name} and {age}")
pos("Shreya",25)

def kwrds(name,age):

    print(f"hi im {name} and {age}")
kwrds(name="Bonkers",age=2)
kwrds(age=1,name="Bonky")

#postional arguments with keyword
def pos_key(name,age):
    print("Hello", name ,age)
pos_key("Deepika",age=25)
# pos_key(age=25, "Deepika") #SyntaxError: positional argument follows keyword argument
# pos_key(name="Deepika",age=25) #SyntaxError: positional argument follows keyword
#default arguments
def f3(a=10,b=10):
    print(a,b)
f3(12,2)

#varibale length arguments - args()
def f4(*args):
    for i in args:
        print(i*i)
f4(1,2,3,4)
#variable length arguments - kwargs()
def f5(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} is {value}")
f5(name="Deepika",age=25,city="Banglore")


#function- block of cde
#module- group of functiobns in a saved file
#pakages/library- group of modules