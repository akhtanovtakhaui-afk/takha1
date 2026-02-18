
add = lambda a, b: a + b
print(add(3, 7))

sq = lambda x: x * x
print(sq(5))

is_even = lambda x: x % 2 == 0
print(is_even(10))
print(is_even(11))

length = lambda s: len(s)
print(length("KBTU"))

bigger = lambda a, b: a if a > b else b
print(bigger(9, 4))
