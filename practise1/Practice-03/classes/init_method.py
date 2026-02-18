
class User:
    def __init__(self, name):
        self.name = name

u = User("Alibek")
print(u.name)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.x, p.y)

class Car:
    def __init__(self, brand, year=2020):
        self.brand = brand
        self.year = year

c1 = Car("Toyota")
c2 = Car("BMW", 2022)
print(c1.brand, c1.year)
print(c2.brand, c2.year)

class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.area = w * h

r = Rectangle(5, 2)
print(r.area)

class Group:
    def __init__(self, members):
        self.members = members

g = Group(["Ali", "Dana"])
print(g.members)
