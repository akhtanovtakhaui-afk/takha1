
a = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, a))
print(evens)

a = [-3, 0, 5, -1, 9]
pos = list(filter(lambda x: x > 0, a))
print(pos)

words = ["ai", "ml", "python", "code"]
longs = list(filter(lambda s: len(s) >= 4, words))
print(longs)

words = ["gas", "oil", "water", "steam"]
has_a = list(filter(lambda s: "a" in s, words))
print(has_a)

a = [0, 1, "", "hi", None, 5]
truthy = list(filter(lambda x: bool(x), a))
print(truthy)
