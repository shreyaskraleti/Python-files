#1Write a Python script that utilizes the len(), max(), min(), and
#sum() functions on a list of integers. Explain what each function does.

a =[12,3,4,5,45,60]
print("Length of the list:", len(a)) #to find the no of elements
print("Maximum value in the list:", max(a)) #to find the max no in the list
print("Minimum value in the list:", min(a)) #to find the min no in the list
print("Sum of all values in the list:", sum(a)) #sum of the elments

#2.Define a function named greet() that takes a string as an
# argument and prints a greeting message using that string. Call
# this function with different names.

def greet(name):
    print(f"Hi {name}")
greet("Deepika")
greet("Shreya")
greet("Bonkers")

# 3.Create a function named square() that takes an integer as an
# argument, calculates its square, and returns the result. Print the
# returned value.

def square(num):
    return num ** 2
print(square(5))
# 4. Write a function describe_pet() that takes two arguments: the
# name of a pet and its type. Set the default type to 'dog'. Test this
# function by passing different arguments.

def describe_pet(name,type="dog"):
    print(f"Name  is {name}  type is {type} ")
describe_pet("Bonkers")
describe_pet(name="Bonky",type="shihtzu")

# 5.Create a function build_profile() that takes in first and last
# names as well as an arbitrary number of keyword arguments
# (**kwargs). Return a dictionary representing the user’s profile.

def build_profile(**kwargs):
    for keys,value in kwargs.items():
        print(f"{keys} : {value}")
build_profile(first_name="Deepika", last_name="Vemuri")

# 6.Write a function sum_all() that takes any number of numerical
# arguments and returns their sum. Test it with different numbers
# of arguments.       
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4))
print(sum_all(10,20,30,40))

# 7. Define a function modify_list() that takes a list and appends a
# new element to it. Call this function and print the list before and
# after the modification.

def modify_list(lst):
    print("Orininal list",lst)
    lst.append(5)
    return lst
print(modify_list([1,2,3]))
# 8. Write a function calculate() that takes two numbers and returns
# their sum, difference, and product. Call this function and print
# the results.

def calculate(n1,n2):
    sum = n1+n2
    diff = n1-n2
    prd = n1*n2
    return sum,diff,prd
a,b,c = calculate(30,10)
print("Tha add is:", a)
print("The differnce is:",b)
print("The product is:",c)

# 9. Create a function order_pizza() that takes arguments for crust
# type, size, and a list of toppings. Ensure that the crust type and
# size are passed as positional arguments and toppings as a
# keyword argument.
def order_pizza(crust,size,toppings):
    print(f"The crust is {crust} and its {size} pizaa with toppings {toppings}")
order_pizza("Wheat-thin Crust","medium",toppings=["olive","panner"])

# 10. Write a function describe_person() that takes two arguments:
# name and age, where age has a default value of None. If age is
# provided, print the name and age; otherwise, print only the
# name.
    
def describe_person(name,age= None):
    if age == None:
        print(f"My name is {name}")
    else:
        print(f"My name is {name} and age is{age}")
describe_person("Aarav")
describe_person("Aarav",10)














 
    

  