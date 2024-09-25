# Inheritance:
#   - A class can inherit properties and methods from another class.
#   - The child class inherits all the attributes and methods of the parent class.
#   - The child class can also add new attributes and methods or override the ones inherited from the
#     parent class.
#   - Inheritance is used to create a hierarchy of classes where a child class is a modified version of the parent class.
#   - Inheritance is used to promote code reusability and reduce code duplication.

# Types of Inheritance:
#   - Single Inheritance: A child class inherits from a single parent class.
#   - Multiple Inheritance: A child class inherits from multiple parent classes.
# -Multilevel Inheritance: A child class inherits from a parent class, and the parent class inherits from grandparent class.
#   - Hierarchical Inheritance: A parent class can have multiple child classes.
#   - Hybrid Inheritance: A combination of multiple inheritance and multilevel inheritance.


# Single Inheritance:
class Parent:
    def f1(self):
        print("this is parent class")

class Child(Parent):
    def f2(self):
        print("this is child class")
        
c = Child()
c.f2()
c.f1() # we can access both parent and child by using child object

p = Parent()
p.f1() # we cannot access child by using parent object

class Teacher:
    def f1(self):
        print("Teacher is teaching the subjects")
class Student(Teacher):
    def f2(self):
        print("Student is learning the subjects")
s = Student()
s.f2()
s.f1()
t = Teacher()
t.f1()


#Multilevel:
class GrandParent:
    def f1(self):
        print("this is grandparent class")
        
class Parent(GrandParent):
    def f2(self):
        print("this is parent class")
        
class Child(Parent):
    def f3(self):
        print("this is child class")
        
c = Child()
c.f3()
c.f2()
c.f1()
p = Parent()
p.f2()
p.f1()
g = GrandParent()
g.f1()

class GrandFather():
    def f1(self):
        print("GrandFather is a man")
class Father(GrandFather):
    def f2(self):
        print("Father is a man")
class Son(Father):
    def f3(self):
        print("Son is a man")
s = Son()
s.f3()
s.f2()
s.f1()
f = Father()
f.f2()
f.f1()
g = GrandFather()
g.f1()


# using Super method:
class Animal:
    def __init__(self,name,age):
        self.n = name
        self.a = age
        
    def sound(self):
        print(f"my name is {self.n} and my age is {self.a} and i make sound")

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.b = breed
        
    def sound(self):
        super().sound()
        print(f" iam a dog of breed {self.b}")

# creating an object of Dog class
d = Dog("bonkers", 2 ,"shitzu")
d.sound()  # Output: my name is bonkers and my age is 2 and i
a = Animal("chocolate", 3)
a.sound()
# Output: my name is chocolate and my age is 3 and i make sound

class Course1:
    def __init__(self,name,category):
        self.n = name
        self.c = category
    def f1(self):
        print(f" course name is {self.n} and category is {self.c}")
        
class Course2(Course1):
    def __init__(self,name,category):
        super().__init__(name,category)
       
    def f2(self):
        super().f1()
        print("iam learning the course")
        
c2 = Course2("Python", "Back-end")
c2.f2()
c2.f1()

c1 = Course1("Html", "Front-end")
c1.f1()

class Student1():
    def __init__(self,name,age,id):
        self.n = name
        self.a = age
        self.i = id
    def f1(self):
        print(f"my name is {self.n} my age is {self.a} my id is {self.i}")
class Student2(Student1):
    def __init__(self,name,age,id):
        super().__init__(name,age,id)
    def f2(self):
        super().f1()
        print("Student2 is good at sports")
s2 = Student2("Phani",12,3)
s2.f2()
s2.f1()
s1 = Student1("shreya",10,2)
s1.f1()





