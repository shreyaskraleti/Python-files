# copy
dict1 = {"a":10, "b": 12}
dict2 = dict1.copy()
print(dict2)

# assign = 
dict1 = {"a":10, "b": 12}
dict2 = dict1
print(dict2)

# dict constructor
dict1 = {"a":10, "b": 12}
dict2 = dict(dict1)
print(dict2)

# items
dict1 = {"a":10, "b": 12}
dict2 = dict1.items()
print(dict2)
dict2 = dict(dict1.items())
print(dict2)

# sorting
dict1 = {"c":15, "a": 2, "b": 10}
dict2 = sorted(dict1.items())
print(dict2)
dict3 = sorted(dict1)
print(dict3)
dict4 = sorted(dict1.values())
print(dict4)

#max, min and length
dict1 = {"a":10, "b": 12, "c": 15}
print(max(dict1)) # max value
print(min(dict1)) # min value
print(len(dict1)) # length 

dict2 = {"c":21, "a": 10, "b": 300, "d": 3000, "f": 2000}
print(max(dict2))
print(min(dict2))
print(len(dict2))
