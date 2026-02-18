
class Animal:
    def sound(self):
        print("...")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()

class Calculator:
    def calc(self, a, b):
        return a + b

class MulCalculator(Calculator):
    def calc(self, a, b):
        return a * b

m = MulCalculator()
print(m.calc(3, 4))

class Logger:
    def log(self, msg):
        print("LOG:", msg)

class FileLogger(Logger):
    def log(self, msg):
        super().log(msg)
        print("Saved")

f = FileLogger()
f.log("hello")

class Box:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __str__(self):
        return f"Box({self.w}, {self.h})"

b = Box(3, 5)
print(b)

class Group:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

g = Group(["A", "B", "C"])
print(len(g))
