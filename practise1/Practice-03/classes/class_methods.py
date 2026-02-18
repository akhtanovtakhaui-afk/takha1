
class Student:
    school = "KBTU"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, s):
        x, y = map(int, s.split(","))
        return cls(x, y)

p = Point.from_string("10,20")
print(p.x, p.y)

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def how_many(cls):
        print(cls.count)

a = Counter()
b = Counter()
Counter.how_many()

class Config:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def local(cls):
        return cls("localhost", 8080)

cfg = Config.local()
print(cfg.host, cfg.port)

class App:
    mode = "dev"

    @classmethod
    def set_mode(cls, m):
        cls.mode = m

print(App.mode)
App.set_mode("prod")
print(App.mode)
