
class User:
    pass

u = User()
print(u)

class Greeter:
    def say_hi(self):
        print("Hi!")

g = Greeter()
g.say_hi()

class Box:
    pass

b = Box()
b.w = 3
b.h = 4
print(b.w * b.h)

class Calculator:
    def add(self, a, b):
        print(a + b)

c = Calculator()
c.add(5, 7)

class Person:
    def info(self, name):
        print("Name:", name)

p1 = Person()
p2 = Person()
p1.info("Ali")
p2.info("Dana")