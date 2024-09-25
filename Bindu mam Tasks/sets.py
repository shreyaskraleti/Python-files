# sets:
# set is unordered, unindexed, immutable, doesnt allow duplicates, {}

a = {1,2,3,"shreya", 5, "bonky"}
print(a) # unordered output

print(type(a)) # set

# a = {1,2,3,"shreya", 5, "bonky"}
# print(a[1]) # unindexed

# a = {1,2,3,"shreya", 5, "bonky"}
# a[3] = "phani"
# print(a) # immutable

a = {1,2,3,"shreya", 5, "bonky", "shreya", 1, 2, 3, 1, 2}
print(a) # doesnt allow duplicates in output

# Set Methods:
# add(), clear(), copy(), difference(), difference_update(), discard(), intersection(), intersection_update(), is
# subset(), isdisjoint(), union(), issuperset(), pop(), remove(), symmetric_difference

#union:
a = {1,2,3,"shreya", 5, "bonky"}
b = {4,5,6,1,2,3,"shreya"}
print(a.union(b))

#intersection:
a = {1,2,3,"shreya","bonky"}
b = {4,5,6,1,2,3,"shreya"}
print(a.intersection(b))

#update:
a = {1,2,3,"shreya","bonky"}
b = {4,5,6,1,2,3,"shreya"}
a.update(b)
print(a)

#discard:
a = {1,2,3,"shreya","bonky"}
a.discard(3)
print(a)
a.discard("shreya")
print(a)

#pop:
a = {1,2,3,"shreya","bonky"}
print(a.pop()) # random element is popped
print(a.pop())
print(a)

#remove:
a = {1,2,3,"shreya","bonky"}
a.remove(1)
print(a)
a.remove(3)
print(a)

#copy:
a = {1,2,3,"shreya","bonky"}
b = a.copy()
print(b)

a = {1,23,34,5,72}
b = a.copy()
print(b)

#issubset:
a = {1,2,3,4,5}
b = {1,2,3,4,5,6,7,8,9}
print(a.issubset(b))

a = {"shreya", "bonky"}
b = {"shreya", "deepu", "phani", "bonky"}
print(a.issubset(b))

#issuperset:
a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,4,5}
print(a.issuperset(b))

a = {23,34,56,78}
b = {23,34}
print(a.issuperset(b))

#difference:
a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,10,11,12}
print(a.difference(b))

a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,10,11,12}
print(b.difference(a))

#symmetric difference:
a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,10,11,12}
print(a.symmetric_difference(b))

a = {12, 23, 34, 45, 56}
b = {34, 45, 56, 67, 78, 89}
print(a.symmetric_difference(b))

#add:
a = {1,2,3}
a.add("hello shreya and bonky")
print(a)

a = {1,2,3}
a.add(5)
print(a)

#clear:
a = {1,2,3,4,5,6,7,8,9}
a.clear()
print(a)

a = {1,2,3,4,5,6,7,8,9, 10, 11, 12}
a.clear()
print(a)