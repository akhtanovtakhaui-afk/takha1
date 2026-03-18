with open("example.txt", "w") as f:
    f.write("Hello World\n")

with open("example.txt", "w") as f:
    f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

with open("example.txt", "a") as f:
    f.write("New line added\n")

with open("numbers.txt", "w") as f:
    for i in range(1, 6):
        f.write(str(i) + "\n")

text = input("Enter text: ")
with open("user.txt", "w") as f:
    f.write(text)
