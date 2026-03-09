#1
import os

os.makedirs("test/dir1/dir2", exist_ok=True)
#2
import os

for item in os.listdir("."):
    print(item)
#3
import os

for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)
#4
import shutil

shutil.move("sample.txt", "test/sample.txt")