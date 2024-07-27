# dictionay :
# key : value pairs separated by colon
# ordered/unordered, mutable, doesnt support duplicates, follows index, {}
# access the data using keys, value doesnt have identity in dictionary
# dictionary is mutable
# if we access by value it will return errors.

# dictionary methods:
# 1. dict() : creates a dictionary
# 2. fromkeys() : creates a dictionary from keys and values
# 3. get() : returns the value of the key
# 4. items() : returns the key value pairs
# 5. keys() : returns the keys of the dictionary
# 6. values() : returns the values of the dictionary
# 7. pop() : removes the key value pair
# 8. popitem() : removes the last inserted key value pair

a = {}
print(type(a))

dict = {"apple":1, "grapes": 2}
print(type(dict))

for i in dict:
    print(i)
    
print(dict["apple"])
print(dict.get("grapes"))

# value can be changed
dict["apple"] = 5
print(dict)

# key can be changed
dict["mango"] = dict.pop("grapes") # pop to remove the key
print(dict)

mydict = {"name": "shreya", "age": 30, "place": "bangalore"}
print(len(mydict))

for i in mydict:
    print(i)
    
print(mydict.get("name"))
print(mydict.get("place"))

#keys()
print(mydict.keys())

#values()
print(mydict.values())

#items()
print(mydict.items())

#pop() # removes the key value pair as per the key passed by us
print(mydict.pop("age"))
print(mydict)

#popitem() removes the last key value pair
mydict.popitem()
print(mydict)

# value doesnt have identity
dict = {"apple":1, "banana":2, "grapes":3}
for i in dict:
    print(dict[i])

# we can access by key
dict = {"apple":1, "banana":2, "grapes":3}
for i in dict:
    print(i)
    
# adding new key-value pair inside the dict
dict = {"apple":1, "banana":2, "grapes":3}
dict["orange"] = 4
print(dict)
dict["pappaya"] = 5
print(dict)

#using update()
dict = {"apple":1, "banana":2, "grapes":3}
dict.update({"orange":4})
print(dict)
dict.update({"pappaya":5})
print(dict)

#del
del dict["pappaya"]
print(dict)
del dict["grapes"]
print(dict)

#clear - elements will be removed but structure will be present
dict = {"apple":1, "banana":2, "grapes":3}
dict.clear()
print(dict)
del dict
print(dict)

# adding two dicts
dict1 = {"apple":1, "banana":2}
dict2 = {"grapes":3, "guava":4}
dict1.update(dict2)
print(dict1)
    
# in dict it doesnt support duplication of data at keys position where as values can be same
dict = {"apple":1, "banana":2, "guava":3, "grapes":4, "apple":21}
print(dict)
dict = {"apple":1, "banana":2, "guava":4, "grapes":4,}
print(dict)
dict1 = {"a":10, "a": 12}
print(dict1)

# using keyword arguments ** to add more than two dictionaries:
dict1 = {"a":10, "b": 12}
dict2 = {"c":13, "d": 14}
dict3 = {"e":15, "f": 16}
final_dict = {**dict1, **dict2, **dict3}
print(final_dict)

