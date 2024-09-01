# odd or even
num = 25
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# greatest of 3 numbers:
a = 10
b = 22
c = 15
if (a > b and a > c):
    print(a, "is greater")
elif (b > a and b > c):
    print(b, "is greater")
else:
    print(c, "is greater")

# greatest of 4 numbers:
a = 13
b = 17
c = 67
d = 90
if (a > b and a > c and a > d):
    print(a, "is greater")
elif (b > a and b > c and b > d):
    print(b, "is greater")
elif (c > a and c > b and c > d):
    print(c, "is greater")
else:
    print(d, "is greater")

# multiple of 7:
a = int(input("enter your number: "))
if (a % 7 == 0):
    print(a, "is multiple of 7")
else:
    print(a, "is not multiple of 7")
