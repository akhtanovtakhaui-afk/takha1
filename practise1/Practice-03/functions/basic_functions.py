
def greet():
    print("Hello!")

greet()

def greet_name(name):
    print("Hello,", name)

greet_name("Ali")

def add(a, b):
    print(a + b)

add(3, 7)

def my_max(a, b):
    if a > b:
        print(a)
    else:
        print(b)

my_max(10, 5)

def print_evens(nums):
    for x in nums:
        if x % 2 == 0:
            print(x)

print_evens([1, 2, 3, 4, 5, 6])
