# list:
a = [1,2,3,4,5]
print(type(a))
print(len(a))
print(a[1])
print(a[4])
a[2] = 7
print(a)
a[3] = 9
print(a)

# # strings are immutable
# b = "hi bonky, how are you"
# print(b)
# b["hi"] = "hello"
# print(b)

# lists are mutable
a = [22,33,44,55,12]
a[2] = 25
print(a)

# slicing - positive and negative
a = [11,23,43,34,25,67]
print(a[1:4])
print(a[:5])
print(a[:1])
print(a[1:])
print(a[-4:-1])
print(a[-5:-3])
print(a[::-1]) # reverse
print(a[::2])
print(a[::3])
print(a[2:])

# list methods:
# append, extend, insert, remove, pop, index, count, sort, reverse, copy
# append:
a = [1,2,3,4,5]
a.append(8)
print(a)

a = [12, 2, 23, 4, 1]
a.sort()
print(a)

a = [25, 34, 12, 2, 3, 67, 99]
a.sort(reverse=True)
print(a)