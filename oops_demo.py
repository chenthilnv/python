# Basic class
class Animal:
    def __init__(self, name):
        self.name = name  # public attribute

    def speak(self):
        return f"{self.name} makes a sound"

# Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Encapsulation (private/protected)
class Person:
    def __init__(self, name, age):
        self._name = name         # protected attribute
        self.__age = age          # private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

# Polymorphism
def animal_sound(animal):
    print(animal.speak())

# Class method and static method
class MathUtils:
    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Properties
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

# Magic methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Usage examples
a = Animal("GenericAnimal")
d = Dog("Rex")
animal_sound(a)
animal_sound(d)

p = Person("Alice", 30)
print("Person age (getter):", p.get_age())
p.set_age(35)
print("Person age (setter):", p.get_age())

print("Class method add:", MathUtils.add(2, 3))
print("Static method multiply:", MathUtils.multiply(2, 3))

c = Circle(5)
print("Circle radius:", c.radius)
print("Circle area:", c.area)
c.radius = 10
print("Updated circle area:", c.area)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print("Vector addition:", v3)
