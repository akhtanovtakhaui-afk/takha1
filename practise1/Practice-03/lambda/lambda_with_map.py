
a = [1, 2, 3, 4]
b = list(map(lambda x: x * x, a))
print(b)

a = [5, 10, 15]
b = list(map(lambda x: x + 10, a))
print(b)

words = ["oil", "gas", "kbtu"]
up = list(map(lambda s: s.upper(), words))
print(up)

x = [1, 2, 3]
y = [10, 20, 30]
z = list(map(lambda a, b: a + b, x, y))
print(z)

kzt = [1000, 2500, 5000]
usd = list(map(lambda t: round(t / 500, 2), kzt))
print(usd)
