#1
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
#2
while True:
    x = int(input())
    if x < 0:
        continue
    print(x)
#3
count = 0
while count < 5:
    x = int(input())
    if x <= 0:
        continue
    print(x)
    count += 1
#4
i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1
#5
while True:
    text = input()
    if text == "":
        continue
    print(text)