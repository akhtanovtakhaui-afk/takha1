
a = [5, 2, 9, 1]
print(sorted(a))

a = [5, 2, 9, 1]
print(sorted(a, reverse=True))

words = ["python", "ai", "ml", "coding"]
print(sorted(words, key=lambda s: len(s)))

pairs = [("A", 3), ("B", 1), ("C", 2)]
print(sorted(pairs, key=lambda x: x[1]))

students = [
    {"name": "Ali", "score": 75},
    {"name": "Dana", "score": 90},
    {"name": "Aruzhan", "score": 82},
]
print(sorted(students, key=lambda d: d["score"], reverse=True))
