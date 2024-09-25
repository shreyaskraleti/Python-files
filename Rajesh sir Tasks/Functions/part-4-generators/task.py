# # 12.Create a custom iterator that iterates over a list in reverse order. Test
# it with a list of 5 elements.
import itertools


def reverse(lst):
    index = len(lst) - 1
    while index >= 0:
        yield lst[index]
        index -= 1


list2 = [1, 2, 3, 4, 5]
x = reverse(list2)
for i in x:
    print(i)

# # 13.Write an iterator class that generates the square of numbers from 1 to
# n. Test the iterator by printing the squares of numbers from 1 to 10.


def square(n):
    for i in range(1, n+1):
        yield i ** 2


for i in square(10):
    print(i)


# # 14.Implement a custom iterator that takes a list and iterates over its
# elements indefinitely in a cyclic manner. Test it by printing the first 20
# elements from a list of 4 items.
def custom(lst):
    i = 0
    while True:
        yield lst[i % len(lst)]  # cyclic iteration
        i += 1


list3 = [1, 2, 3, 4]
x = custom(list3)
for i in range(20):
    print(next(x))

# # 10.Write a generator function that yields all permutations of a given list.
# Test it with a list of 3 elements.


def permutation(lst):
    for i in itertools.permutations(lst):
        yield i


list4 = [1, 2, 3]
x = permutation(list4)
for i in x:
    print(i)


# # 15.Create an iterator class that reads a text file word by word. Use this
# iterator to count the number of words in a given file.
