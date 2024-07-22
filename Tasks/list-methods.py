# list methods:
# append, extend, insert, remove, pop, clear, index, count, sort, reverse, del, copy

# append - adds element to end
a = [1,2,3,4,5]
a.append(8)
print(a)

a = ['shreya', 'bonky']
a.append('phani')
print(a)

# insert - adds element based on index given
a = [1,2,3,4,5]
a.insert(2,7)
print(a)

a = ['apple', 'banana']
a.insert(2, 'grapes')
print(a)

# extend - 
a = ['apple', 'grapes']
a.extend('banana')
print(a)

a = ['apple', 'grapes']
a.extend('kiwi')
print(a)

# a = [1,2,3]
# a.extend(4)
# print(a) # int is not iterable only string is iterable

#pop

a = [1,2,3,4]
a.pop()
print(a)

a = [1,2,3,4]
a.pop(1) # removes element based on given index position
print(a)

a = [1,2,3,4]
a.pop(3) # removes element based on given index position
print(a)

# remove: removes the given element from list
a = [1,2,3,4,5,6,7,8,9]
a.remove(9)
print(a)

a = [1,2,3,4,5,6,7,8,9]
a.remove(7)
print(a)

a = [1,2,3,4,5,6,7,8,9]
a.remove(3)
print(a)

# sort: gives the default output in ascending order
# sort(reverse = True): gives the output in descending order
a = [23, 12, 34, 56, 12, 13, 18, 1, 2]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = [12, 1, 2, 51, 23, 67, 13]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# reverse: elements in reverse order
a = [12, 1, 2, 51, 23, 67, 40, 3]
a.reverse()
print(a)

a = [1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)

# count: counts the no. of elements
a = [1,2,3,4,4,4,5,4,6,7,3,3,3,2,2,4,5,4,5,6,7,8]
print(a.count(4))
print(a.count(3))
print(a.count(6))

# index: first index of given element
a = [1,2,3,4,4,4,5,4,6,7,3,3,3,2,2,4,5,4,5,6,7,8]
print(a.index(3))
print(a.index(4))

# clear: elements are cleared but data structure will be available
a = [1,2,3,4,4,4,5,4,6]
a.clear()
print(a)

# del - deletes the elements as well as structure
a = [1,2,3,4,4,4,5,4,6]
del a

# copy:
a = [1,2,3,4,4,4,5,4,6]
b = a.copy()
print(b)

a = ['shreya']
b = a.copy()
print(b)

