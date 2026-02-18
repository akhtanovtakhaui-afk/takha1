
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

s = Student("Ali", 3.5)
print(s.name, s.gpa)

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

b = B()
b.show()

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

class PremiumAccount(Account):
    def deposit(self, amount):
        super().deposit(amount)
        self.balance += 10

p = PremiumAccount(100)
p.deposit(50)
print(p.balance)

class X:
    def ping(self):
        print("X")

class Y(X):
    def ping(self):
        super().ping()
        print("Y")

class Z(Y):
    def ping(self):
        super().ping()
        print("Z")

z = Z()
z.ping()

class Device:
    def __init__(self, id_):
        self.id_ = id_

class Phone(Device):
    def __init__(self, id_, model):
        super().__init__(id_)
        self.model = model

p = Phone(7, "iPhone")
print(p.id_, p.model)
