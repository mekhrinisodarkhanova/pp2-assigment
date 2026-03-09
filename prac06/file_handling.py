#1 Создать файл и записать данные
with open("sample.txt", "w") as f:
    f.write("Hello\n")
    f.write("Python\n")
    f.write("File handling\n")
#2 Прочитать и вывести файл
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())
#3 Добавить строки в файл
with open("sample.txt", "a") as f:
    f.write("New line 1\n")
    f.write("New line 2\n")

with open("sample.txt") as f:
    print(f.read())
#4 Копировать файл (shutil)
import shutil

shutil.copy("sample.txt", "backup.txt")
print("File copied")
#5 Удалить файл
import os

if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("File deleted")