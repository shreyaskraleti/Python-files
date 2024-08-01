# oops concepts:
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism
# 5. Composition
# 6. Command
# 7. Observer
# 8. Strategy
# 9. Template Method
# 10. Factory Method
# 11. Singleton
# 12. Adapter
# 13. Bridge
# 14. Composite
# 15. Decorator
# 16. Facade

# init method:
# - used to initialize the object
#   - called when an object is created from a class
#   - used to set the initial state of the object
#   - can be used to perform any necessary setup or initialization
#   - can be used to set default values for attributes
#   - can be used to perform any necessary validation or error checking

# self keyword:
# - used to refer to the current instance of the class
#   - used to access attributes and methods of the class
#   - used to pass the instance as an argument to methods
#   - used to return the instance from methods

# class:
# - a blueprint or template for creating objects
#   - defines the properties and behavior of an object
#   - used to group related data and methods together
#   - used to create multiple objects that share the same properties and behavior

class Person:
    def __init__(self,name,age,address):
        self.n = name
        self.a = age
        self.ad = address
    
p = Person("shreya", 30, "bangalore")
print(p.n)
print(p.a)
print(p.ad)

class Employee:
    def __init__(self,name,age,id,salary):
        self.n = name
        self.a = age
        self.id = id
        self.s = salary
        
    def display(self):
        return f"employee name is {self.n} id is {self.id} and salary is {self.s}"

e = Employee(name = "shreya", age = 30, id = 12, salary = 20000)
print(e.display())

class Student:
    def __init__(self, name, id):
        self.n = name
        self.i = id
s = Student("shreya", 15)
print(s.n)
print(s.i)

class Course:
    s1 = "python"
    s2 = "html"
    s3 = "css"
    s4 = "javascript"
    
print(Course.s2)
print(Course.s4)

class Student:
    def __init__(self, name, id):
        self.n = name
        self.i = id
    def display(self):
        return f"student name is {self.n} and id is {self.i}"
s = Student("shreya", 15)
print(s.n)
print(s.i)
print(s.display())
           