# # 1. Write a generator function that yields the Fibonacci sequence up to a
# given number n. Test the generator by printing the first 10 numbers in
# the sequence.
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


x = fibonacci(10)
# Test the generator
for i in x:
    print(i)

# # 2. Create a generator that yields an infinite sequence of natural numbers
# starting from 1. Use next() to print the first 20 numbers.


def infinite_sequence(n):
    num = 1
    while True:
        yield num
        num += 1


x = infinite_sequence(30)
for i in range(20):
    print(next(x))

# # 6. Write a generator that yields the factorial of numbers starting from 1
# up to n. Test the generator by printing the factorials of the first 10
# numbers.


def factorial(n):
    num = 1
    for i in range(1, n+1):
        yield num
        num *= i


g = factorial(10)
for i in g:
    print(i)

# # 7. Create a generator that counts down from a given number to 0,
# yielding each number. Test it by counting down from 10.


def count_down(n):
    while n >= 0:
        yield n
        n -= 1


x = count_down(10)
for i in range(10):
    print(next(x))

# # 8. Write a generator that takes a list and yields its elements in a circular
# manner (i.e., it should loop over the list indefinitely). Test it by printing
# the first 15 elements from a list of 5 items.


def circular(list1):
    i = 0  # index is 0
    while True:
        yield list1[i]
        # when i reaches length of list then it goes back to o and circular loop is generated
        i = (i+1) % len(list1)


list1 = [1, 2, 3, 4, 5]
x = circular(list1)
for i in range(15):
    print(next(x))

# # 9. Create a generator that yields powers of two (e.g., 1, 2, 4, 8, 16, …) up
# to a certain number n. Use this generator to print powers of two up to 2^10.


def power(n):
    pow = 0
    while pow <= n:
        yield 2 ** pow
        pow += 1


x = power(10)
for i in x:
    print(i)


# # 11.Implement a custom iterator class that iterates over a list and yields
# only even numbers. Test it with a list containing both even and odd
# numbers.
def iterator(list1):
    for i in list1:
        if i % 2 == 0:
            yield i


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = iterator(list1)
for i in x:
    print(i)
