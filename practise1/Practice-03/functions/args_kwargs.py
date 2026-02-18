
def sum_all(*args):
    s = 0
    for x in args:
        s += x
    return s

print(sum_all(1, 2, 3))
print(sum_all(10, 20))

def max_all(*args):
    m = args[0]
    for x in args:
        if x > m:
            m = x
    return m

print(max_all(5, 1, 9, 2))

def show_profile(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)

show_profile(name="Alibek", age=19, city="Atyrau")

def report(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

report(1, 2, 3, a=10, b=20)

def settings(**kwargs):
    theme = kwargs.get("theme", "light")
    lang = kwargs.get("lang", "kz")
    print(theme, lang)

settings(theme="dark")
settings(lang="ru")
settings(theme="dark", lang="en")
