# recursion:
#   - recursive function calls itself
#  1. Write a recursive function to calculate the factorial of a given number.
def factorial(n):
    # base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)
r1 = factorial(5)
r2 = factorial(6)
r3 = factorial(7)
print(r1)
print(r2)
print(r3)

# 2. Create a recursive function that returns the nth Fibonacci number.
def fibonacci(n):
    # base case: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)
f1 = fibonacci(2)
f2 = fibonacci(3)
f3 = fibonacci(10)
print(f1)
print(f2)
print(f3)

# 3. Write a recursive function to calculate the sum of digits of a given integer.
def sum_digit(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digit(num // 10)
num = 67892
print(sum_digit(num))

# 4. Implement a recursive function to reverse a given string. 
def reverse(s):
    # base case: empty string is already reversed
    if len(s) == 0:
        return s
    # recursive case: reverse the rest of the string and append the first character
    else:
        return s[-1] + reverse(s[:-1])
s1 = "hello"
s2 = "world"
print(reverse(s1))
print(reverse(s2))

# 5. Create a recursive function to check if a given string is a palindrome. 
def palindrome(s):
    # base case: empty string or single character is a palindrome
    if len(s)<=1:
        return True
    # recursive case: check if the first and last characters are the same, and the rest of
    # the string is a palindrome
    elif s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False
res = palindrome("mom")
res1 = palindrome("dad")
res2 = palindrome("queen")
print(res)
print(res1)
print(res2) 

# 10.Create a recursive function to count the number of vowels in a given string.
def count(s):
    if len(s) == 0:
        return 0
    else:
        vowels = 'aeiouAEIOU'
        if s[0] in vowels:
            return 1 + count(s[1:])
        else:
            return count(s[1:])
text = "shreya"
print(count(text))
string1 = "phani"
print(count(string1))

# 11.Write a recursive function to find the minimum element in a list of numbers.
def find_min(lst1):
    if len(lst1) == 1:
        return lst1[0]
    else:
        return min(lst1[0], find_min(lst1[1:]))
lst1 = [11,22,3,4,55,6]
res = find_min(lst1)
print(res)

# 12.Implement a recursive function to count the occurrences of a specific element in a list. 
def count(lst2, element):
    if len(lst2) == 0:
        return 0
    else:
        if lst2[0] == element:
            return 1 + count(lst2[1:], element)
        else:
            return count(lst2[1:], element)
lst2 = [2,1,2,3,1,2,3,2,4,5,6,2]
res = count(lst2, 2)
print(res)

# 13.Implement a recursive function to calculate the sum of all even numbers in a list.
def sum_even(lst2):
    if len(lst2) == 0:
        return 0
    else:
        if lst2[0] % 2 == 0:
            return lst2[0] + sum_even(lst2[1:])
        else:
            return sum_even(lst2[1:])
lst2 = [1,2,3,4,5,6]
res = sum_even(lst2)
print(res)

# 14.Implement a recursive function to calculate the sum of all elements in a nested list structure.
def sum_nested(lst):
    total = 0
    for i in lst:
        if isinstance(i, list): # check if it is list
            total += sum_nested(i) # recursively sum the nested list
        else:
            total += i # add the number to the total
    return total
    
lst = [1,[2,3,4],[5,6],7,[8,9],10]
res = sum_nested(lst)
print(res)

# 15.Write a recursive function to determine if a given number is prime.
import math
def pri(a):
    if a <= 1:
        return False
    elif a == 2:
        return True
    elif a % 2 == 0:
        return False
    for i in range(3, math.isqrt(a) + 1, 2):
        if a % i == 0:
            return False
    
    return True
res = pri(5)
print(res)


    
    
            
        
        