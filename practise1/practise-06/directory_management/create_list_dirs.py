import os

os.mkdir("new_folder")

os.makedirs("parent/child/grandchild")

items = os.listdir(".")
print(items)

dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
print(dirs)

files = [f for f in os.listdir(".") if os.path.isfile(f)]
print(files)

