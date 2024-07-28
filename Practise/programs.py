# no. is even or odd:
a = int(input("enter a number:"))
if (a%2==0):
    print("a is even number")
else:
    print("a is odd number")
    
# largest of three numbers:
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if (a>b) and (a>c):
    print("a is largest number")
elif (b>a) and (b>c):
    print("b is largest number")
else:
    print("c is largest number")

