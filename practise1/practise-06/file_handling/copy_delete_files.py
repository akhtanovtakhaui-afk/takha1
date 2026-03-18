import shutil
import os

shutil.copy("source.txt", "copy.txt")

shutil.copy2("source.txt", "copy_with_metadata.txt")

shutil.copytree("folder1", "folder2")

if os.path.exists("copy.txt"):
    os.remove("copy.txt")

if os.path.exists("folder2"):
    shutil.rmtree("folder2")

    