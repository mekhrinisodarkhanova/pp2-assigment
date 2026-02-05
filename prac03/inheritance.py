#1 Parent and child class relationships
class Animal:          # Parent class
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):     # Child class
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # унаследованный метод
d.bark()    # метод дочернего класса
#2 Using super() to call parent methods
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")
d = Dog()
d.speak()
#3 Method overriding
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):          # overriding
        print("Dog barks")
a = Animal()
d = Dog()

a.speak()   # Animal makes a sound
d.speak()   # Dog barks
#4 Multiple inheritance
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass
d = Duck()
d.fly()
d.swim()
#5 Abstract base classes (optional advanced topic)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
c = Circle(5)
print(c.area())