#1
nums = [1,2,3,4,5,6]
even = list(filter(lambda x: x % 2 == 0, nums))
square = list(map(lambda x: x**2, nums))
print(even)
print(square)
#2
from functools import reduce
nums = [1,2,3,4]
total = reduce(lambda x, y: x + y, nums)
print(total)
#3
names = ["Alice","Bob","Tom"]
scores = [90,85,88]
for i, name in enumerate(names):
    print(i, name)
for name, score in zip(names, scores):
    print(name, score)
#4
x = "10"
if isinstance(x, str):
    x = int(x)
print(x + 5)