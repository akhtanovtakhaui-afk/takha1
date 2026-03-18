import shutil
import os

shutil.move("file.txt", "folder/file.txt")

shutil.move("old_name.txt", "new_name.txt")

if os.path.exists("file.txt"):
    shutil.move("file.txt", "folder/file.txt")

for f in os.listdir("."):
    if f.endswith(".txt"):
        shutil.move(f, "texts/" + f)

shutil.move("old_folder", "new_folder")
