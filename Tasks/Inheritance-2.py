# Multiple Inheritance:
# Child Inherits properties from multiple parents.
class Parent1:
    def f1(self):
        print("this is first parent class")
class Parent2:
    def f2(self):
        print("this is second parent class")
class Child(Parent1,Parent2):
    def f3(self):
        print("this is child class")
c = Child()
c.f3()
c.f2()
c.f1()
# Output: this is child class this is second parent class this is first parent class
p2 = Parent2()
p2.f2()

p1 = Parent1()
p1.f1()
# Output: this is second parent class this is first parent class

class Teacher1():
    def f1(self):
        print("this is first teacher class")
class Teacher2():
    def f2(self):
        print("this is second teacher class")
class Teacher3():
    def f3(self):
        print("this is third teacher class")
class Student(Teacher1,Teacher2,Teacher3):
    def f4(self):
        print("this is student class")
s = Student()
s.f4()
s.f3()
s.f2()
s.f1()
t1 = Teacher1()
t1.f1()
t2 = Teacher2()
t2.f2()
t3 = Teacher3()
t3.f3()


#Hierchical Inheritance:
# Multile children inherits properties from single parent.
class Parent:
    def f1(self):
        print("this is parent class")
class Child1(Parent):
    def f2(self):
        print("this is child1 class")
class Child2(Parent):
    def f3(self):
        print("this is child2 class")
c2 = Child2()
c2.f3()
c2.f1()
# Output: this is child2 class this is parent class
c1 = Child1()
c1.f2()
c1.f1()
# Output: this is child1 class this is parent class

class GrandParent():
    def g1(self):
        print("this is grandparent class")
class Parent1(GrandParent):
    def f1(self):
        print("this is first parent class")
class Parent2(GrandParent):
    def f2(self):
        print("this is second parent class")
p2 = Parent2()
p2.f2()
p2.g1()
p1 = Parent1()
p1.f1()
p1.g1()


# Hybrid Inheritance:
# Child inherits properties from parent and grand parent.
# It is a combination of two or more types of inheritance.

class Parent1():
    def f1(self):
        print("this is first parent class")
class Parent2():
    def f2(self):
        print("this is second parent class")
class Child1(Parent1):
    def f3(self):
        print("this is child1 class")
class Child2(Child1, Parent2):
    def f4(self):
        print("this is child2 class")
c2 = Child2()
c2.f4()
# Output: this is child2 class
c2.f3()
# Output: this is child1 class
c2.f2()
# Output: this is second parent class
c2.f1()
# Output: this is first parent class
c1 = Child1()
c1.f3()
# Output: this is child1 class
c1.f1()

class Parent1():
    def f1(self):
        print("this is first parent class")
class Parent2():
    def f2(self):
        print("this is second parent class")
class AnotherParent(Parent1):
    def f3(self):
        print("this is another parent class")
class Child(AnotherParent, Parent2):
    def f4(self):
        print("this is child class")
c = Child()
c.f4()
c.f3()
c.f2()
c.f1()
# Output: this is child class
# this is another parent class
# this is second parent class
# this is first parent class
