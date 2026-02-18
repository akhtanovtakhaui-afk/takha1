
class A:
    def a(self):
        print("A")

class B:
    def b(self):
        print("B")

class C(A, B):
    pass

c = C()
c.a()
c.b()

class Named:
    def __init__(self, name):
        self.name = name

class Aged:
    def __init__(self, age):
        self.age = age

class Person(Named, Aged):
    def __init__(self, name, age):
        Named.__init__(self, name)
        Aged.__init__(self, age)

p = Person("Ali", 19)
print(p.name, p.age)

class X:
    def show(self):
        print("X")

class Y:
    def show(self):
        print("Y")

class Z(X, Y):
    pass

z = Z()
z.show()

class P:
    pass

class Q:
    pass

class R(P, Q):
    pass

print(R.mro())

class CanRun:
    def run(self):
        print("Running")

class CanSwim:
    def swim(self):
        print("Swimming")

class Athlete(CanRun, CanSwim):
    pass

a = Athlete()
a.run()
a.swim()
