# a = "hello"
# b = "shreya"
# print(a+b)

# a = "bonky"
# b = "loves shreya"
# print(a+b)

# c = "shreya loves bonky"
# print(len(c))

# # Indexing
# a = "shreya loves bonky"
# print(a[0])
# print(a[5])
# print(a[10])
# print(a[15])

# b = "bonkers"
# print(b[0])
# print(b[3])

# # Positive Slicing:
# a = "shreya loves bonky"
# print(a[1:5])
# print(a[2:])
# print(a[:10])



# # Negative Slicing:
# a = "shreya loves bonky"
# print(a[-1])
# print(a[-10:-2])
# print(a[-15:-3])
# print(a[-10:])
# print(a[-4:])
# print(a[:-1])
# print(a[:-4])
# print(a[::-1])
# print(a[::-2])
# print(a[::-3])

# # String functions:
# a = "shreya loves bonky"
# print(a.endswith("nky"))
# print(a.capitalize())
# print(a.replace("bonky", "phani"))
# print(a.find("love"))
# print(a.count("a"))
# print(a.index("v"))
# print(a.islower())
# print(a.isupper())

# # program:
# name = input("Enter your name: ")
# print("length of name is: ", len(name))

# a = "hi, $how $$are you$$"
# print(a.count("$"))

# Conditional statements:

marks = int(input("enter marks:"))
if (marks>=90):
    print("grade is A")
elif (marks>=80 and marks<90):
    print("grade is B")
elif (marks>=70 and marks<80):
    print("grade is C")
else:
    print("grade is D")
    
# nesting:
age = int(input("Enter age: "))

if age >= 18:
    if age >= 65:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")



    