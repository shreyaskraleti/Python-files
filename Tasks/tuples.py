# tuple:
# ordered, immutable, allows duplicates, accepts heterogeneous data, denoted by ()

a = (1,2,3,4,5,6,7)
print(type(a))

b = (7,8,9)
c = a+b
print(c)

# Methods:
# count() - returns the number of times a value appears in a tuple
# index() - returns the index of the first value that matches the argument

# count:
a = (1,2,3,1,2,3,1,2,3,4,5,6,7)
print(a.count(2))
print(a)

b = ("apple", "banana", "apple")
print(b.count("apple"))
print(b)

# index:
a = (1,2,3,1,2,3,1,2,3)
print(a.index(2))

b = ("apple", "banana", "apple")
print(b.index("apple"))

# converting into tuple:
a = [11,12,13]
print(tuple(a))

