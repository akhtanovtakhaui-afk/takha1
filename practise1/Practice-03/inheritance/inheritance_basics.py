
class Animal:
    def sound(self):
        print("...")

class Dog(Animal):
    pass

d = Dog()
d.sound()

class Person:
    def hello(self):
        print("Hello")

class Student(Person):
    def study(self):
        print("Studying")

s = Student()
s.hello()
s.study()

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def show(self):
        print(self.brand)

c = Car("Toyota")
c.show()

class MathBase:
    def add(self, a, b):
        return a + b

class MathPro(MathBase):
    def add3(self, a, b, c):
        return self.add(a, b) + c

m = MathPro()
print(m.add3(1, 2, 3))

class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, B))
print(isinstance(b, A))
