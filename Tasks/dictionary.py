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
    

