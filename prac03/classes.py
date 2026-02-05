#1 Class definition and object creation
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)
#2 The __init__() constructor method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
#3 Instance methods and the self parameter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()
#4 Class variables vs instance variables
class Counter:
    count = 0   # class variable

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)  # 3
#5 Modifying and deleting object properties
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Aman", 18)