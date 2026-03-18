
names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names):
    print(i, name)

names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names, start=1):
    print(i, name)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(name, score)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
grades = ["B", "A", "A"]
for name, score, grade in zip(names, scores, grades):
    print(name, score, grade)

keys = ["name", "age", "city"]
values = ["Alice", 20, "Almaty"]
result = dict(zip(keys, values))
print(result)