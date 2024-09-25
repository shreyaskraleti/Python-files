# LEARNED THIS TOPIC FROM CHAT GPT BASED ON 31 JULY QUESTION PAPER AS THIS TOPIC IS NOT AVAILABLE IN RECORDING.

# variable assignments:
#   - `x` is assigned the value of `y`
#   - `y` is assigned the value of `z`

# simple assignment:
x = 10
print(x)
a = "shreya"
print(a)
b = 20
print(b)

# multiple assignment:
#   - `x`, `y`, `z` are assigned the values of `10`,
#     `20`, `30` respectively
x, y, z = 10, 20, 30
print(x,y,z)
a, b, c = 1, 2, 3
print(a,b,c)

# chained assignment:
#   - `x` is assigned the value of `y`
#   - `y` is assigned the value of `z`
#   - `z` is assigned the value of `10`
x = y = z = 10
print(x,y,z)
a = b = c = 1
print(a,b,c)

#unpacking assignment:
list1 = [1,2,3]
a,b,c = list1
print(a,b,c)
# Output: 1 2 3

tuple1 = ("shreya", "30")
name, age = tuple1
print(name,age)
# Output: shreya 30

#augmented assignment:
#   - `x` is assigned the value of `x + 10`
x = 5
print(x)
x += 3
print(x)
x *= 2
print(x)
# Output: 5 8 16


