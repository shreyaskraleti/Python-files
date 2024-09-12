# Variables -  Global ,Local
# Global # The code snippet is demonstrating the concept of global variables in Python. It defines a
# global variable `a` with a value of 10 and then prints the value of `a`. This code simply
# prints the value of the global variable `a`, which is 10.
# Variables

# a = 10
# print(a)

# def sample():
#     print(a)
# sample()


# # Local variables
# def local():
#     b=25
#     print(b)
# local()
# print(b)

# Global keyword

# a = 10
# def f1():
#     a= 44
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()

# #using global keyword
# b =20
# def f3():
#     global b
#     b = 30
#     print("The value is",b)
# def f4():
#     print(b)
# f3()
# f4()

#globals()['index']
c=10
def sample_func():
    c=23
    print(c)
    print(globals()['c'])
sample_func()