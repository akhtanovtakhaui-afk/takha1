from functools import reduce

nums = [1, 2, 3, 4]
result = list(map(lambda x: x**2, nums))
print(result)

nums = [1, 2, 3]
result = list(map(str, nums))
print(result)

nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

nums = [-2, -1, 0, 1, 2]
result = list(filter(lambda x: x > 0, nums))
print(result)

nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums)
print(result)