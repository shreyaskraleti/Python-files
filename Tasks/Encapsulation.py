# Encapsulation:
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
# It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class. Encapsulation also involves restricting direct access to some of an object's components, which is a way of preventing accidental interference and misuse of the methods and data. This is typically achieved by using access specifiers.
# In Python, encapsulation can be implemented using:
# Public members
# Protected members
# Private members
# Key Points
# Encapsulation helps in data hiding and abstraction, ensuring that the internal representation of an object is hidden from the outside. 
# Only the necessary parts are exposed for interaction.
# Public members are accessible from anywhere.
# Protected members are accessible within the class and its subclasses.
# Private members are accessible only within the class and not from outside.

class Add():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def f1(self):
        print(f"a is {self.a} and b is {self.b}")
    def f2(self):
        print(f"Sum of a and b is {self.a + self.b}")
c = Add(2,3)
c.f2()
c.f1()

# In this improved example, the attributes __a and __b are private
# and you use getter and setter methods to access and modify them
# enhancing the encapsulation and control over the internal state of the object.

class Add:
    def __init__(self,a,b):
        self.__a = a # a and b are private attributes
        self.__b = b
        
    def get_a(self):
        return self.__a
    
    def set_a(self, a):
        self.__a = a
        
    def get_b(self):
        return self.__b
    
    def set_b(self, b):
        self.__b = b
        
    def f1(self):
        print(f"a is {self.__a} and b is {self.__b}")
        
    def f2(self):
        print(f"Sum of a and b is {self.__a + self.__b}")
        
c = Add(2,3)
c.f2()
c.f1()

# Accessing private attributes via getter methods
print(c.get_a())
print(c.get_b())

# Modifying private attributes via setter methods
c.set_a(5)
c.set_b(7)
c.f2()
c.f1()
# Accessing private attributes directly is not allowed and will result in an AttributeError