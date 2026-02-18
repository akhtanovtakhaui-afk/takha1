
class A:
    x = 10

print(A.x)
a1 = A()
a2 = A()
print(a1.x, a2.x)

class B:
    y = 5

b1 = B()
B.y = 99
print(b1.y, B.y)

class C:
    z = 1

c1 = C()
c1.z = 100
c2 = C()
print(c1.z)
print(c2.z)

class D:
    items = []

d1 = D()
d2 = D()
d1.items.append(1)
print(d2.items)

class E:
    def __init__(self):
        self.items = []

e1 = E()
e2 = E()
e1.items.append(7)
print(e1.items)
print(e2.items)
