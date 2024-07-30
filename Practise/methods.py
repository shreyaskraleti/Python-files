# list methods:
# 1. append() - adds an element to the end of the list
# 2. insert() - adds an element at a specified position in the list
# 3. remove() - removes the first occurrence of the specified element from the list
# 4. pop() - removes and returns the element at the specified position in the list
# 5. sort() - sorts the list in ascending order
# 6. reverse() - reverses the order of the list
# 7. index() - returns the index of the first occurrence of the specified element in the
# 8. count() - returns the number of occurrences of the specified element in the list
# 9. extend() - adds multiple elements to the end of the list
# 10. clear() - removes all elements from the list
# 11. copy() - returns a copy of the list
# 12. del

#append:
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

#insert:
my_list = [1, 2, 3]
my_list.insert(3,4)
print(my_list)

#remove:
my_list = [1, 2, 3, 4]
my_list.remove(4)
print(my_list)

#pop:
x = [1,2,3,4]
x.pop() # last element will be removed
print(x)
x.pop(1) # based on index element will be removed
print(x)

#sort:
x = [5,3,4,1,2]
x.sort()
print(x)

x = [1,3,2,4,6,5]
x.sort(reverse=True)
print(x)

#reverse:
x = [1,2,3,4,5]
x.reverse()
print(x)

#index:
x = [1,2,3,4,5]
print(x.index(4))

#count:
x = [1,2,2,3,4,4,4,5]
print(x.count(4))

#extend:
x = [1,2,3]
x.extend([4,5,6])
print(x)

#copy:
x = [1,2,3,4,5]
y = x.copy()
print(y)

#clear:
x = [1,2,3,4,5,6]
x.clear()
print(x)

#del:
x = [1,2,3,4,5,6]
del x

# tuple methods:
# count
# index

#count:
t = (1,2,2,3,4,4,4,5)
print(t.count(2))
print(t.count(4))

#index:
t = (1,2,3,1,2,3,4,5,6)
print(t.index(2))
print(t.index(1))
print(t.index(3))

