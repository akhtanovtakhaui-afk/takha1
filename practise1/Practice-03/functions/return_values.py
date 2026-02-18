
def add(a, b):
    return a + b

x = add(10, 20)
print(x)

def is_even(n):
    return n % 2 == 0

print(is_even(6))
print(is_even(7))

def min_max(a, b, c):
    mn = a
    mx = a
    for v in (b, c):
        if v < mn:
            mn = v
        if v > mx:
            mx = v
    return mn, mx

mn, mx = min_max(7, 2, 9)
print(mn, mx)

def word_len(s):
    return len(s)

print(word_len("hello"))

def only_evens(nums):
    res = []
    for x in nums:
        if x % 2 == 0:
            res.append(x)
    return res

print(only_evens([1, 2, 3, 4, 10]))
