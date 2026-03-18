with open("example.txt", "r") as f:
    data = f.read()
    print(data)

with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)

with open("example.txt", "r") as f:
    data = f.read(10)
    print(data)

with open("example.txt", "r") as f:
    line = f.readline()
    print(line)

    