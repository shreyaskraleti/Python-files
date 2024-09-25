# # 1. Basic Decorator Function:
# o Write a decorator that prints "Hello" before executing a function and
# "Goodbye" after executing it.
# o Apply this decorator to a function that prints "World".

import random
import time


def func1(func):
    def inner():
        print("Hello")
        func()
        print("Goodbye")
    return inner


@func1
def func2():
    print("World")


func2()

# 2. Timing Function Execution:
# o Create a decorator that measures the time which a function takes to execute.
# o Apply this decorator to a function that sums numbers from 1 to
# 1,000,000.


def timer(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"execution time: {end_time - start_time} seconds")
    return inner


@timer
def func1():
    total = sum(range(1, 100001))
    print(f" sum of numbers is {total}")


func1()

# # 3. Repeat Execution:
# o Write a decorator that executes a function three times.
# o Test this decorator on a function that prints a given message.


def repeat(func):
    def inner():
        for _ in range(3):
            func()
    return inner


@repeat
def fun1():
    print("Hi Welcome to Achievers It")


fun1()

# # 4. Access Control Decorator:
# o Create a decorator that checks if a user is an admin before allowing the
# execution of a function.
# o If the user is not an admin, print "Access Denied".
# o Test with a simple function that returns a protected message.


def access(func):
    def inner(user, *args, **kwargs):
        if user == "admin":
            return func(user, *args, **kwargs)
        else:
            print(" Access Denied ")
    return inner


@access
def fun1(user):
    return f" hello {user} you have the access"


print(fun1("admin"))
print(fun1("guest"))

# # 5. Decorator with Arguments:
# o Write a decorator that accepts a string argument and prints it before
# executing the function.
# o Apply it to a function that returns a greeting message.


def greet(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@greet("Hi How are you")
def f1():
    print("Welcome to Institute")


f1()

# # 6. Chaining Decorators:
# o Implement two simple decorators (e.g., one that converts the result to
# uppercase and another that doubles the result).
# o Apply both decorators to a single function to demonstrate chaining.


def upper():
    def decor1(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs).upper()
        return wrapper
    return decor1


def doubled():
    def decor2(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * 2
        return wrapper
    return decor2


@upper()
@doubled()
def greet():
    return "Hi Bonkers"


print(greet())

# # 7. Context Management with Decorators:
# o Write a decorator that acts as a context manager, ensuring that a
# resource (e.g., a file) is opened before the function runs and closed
# afterward.
# o Use it to read and print the contents of a file.


def open_file(file_path):
    def decor1(func):
        def wrapper(*args, **kwargs):
            try:
                with open(file_path, 'r') as file:
                    result = func(file, *args, **kwargs)
                    return result
            except FileNotFoundError:
                print(f"file doesnt exist : {file_path} ")
        return wrapper
    return decor1


@open_file(r"C:/Users/Admin/Python-files/Practise/Functions/part-3/file.txt.txt")
def read(file):
    content = file.read()
    print(content)


read()

# # 8. Retry Decorator:
# o Write a decorator that retries a function up to 3 times if it raises an
# exception.
# o Test it on a function that raises an exception with a probability of
# 50%.


def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f" Exception occured: {e}")
                print(f" exception failed after 3 trials ")
    return wrapper


@retry
def prob():
    if random.random() < 0.5:
        raise ValueError("failure")
    return "success"


res = prob()
print(res)

# 9. Decorator for Type Checking:
# o Create a decorator that checks the types of the arguments passed to a
# function.
# o If the types don’t match the expected ones, raise a TypeError.
# o Test it on a function that adds two integers.
# def check(func):
#     def decor1(func):
#         def wrapper(*args, **kwargs):
#             return func(a+b, *args, **kwargs)
#         return wrapper
#     return decor1
# @add
# def f1(a,b):
#     return a+b
# f1(2,4)

# # 10. Decorator for Flattening Nested Lists:
# o Write a decorator that flattens nested lists passed to a function.
# o Apply it to a function that sums all the numbers in a list, including
# nested ones.


def flatten(func):
    def flatten_lst(nested_lst):
        flat_lst = []
        for item in nested_lst:
            if isinstance(item, list):
                flat_lst.extend(flatten_lst(item))
            else:
                flat_lst.append(item)
        return flat_lst

    def wrapper(nested_lst):
        flat_lst = flatten_lst(nested_lst)
        return func(flat_lst)
    return wrapper


@flatten
def sum1(lst):
    return sum(lst)


nested_lst = [1, 2, [3, 4, 5], [5, 6], [7, 8, 9], 10, 11, 12, [13, 14], 15]
res = sum1(nested_lst)
print(res)
