#1
a = -12
b = 7
print(abs(a))
print(max(a, b))
#2
import math
print(math.sqrt(25))
print(math.ceil(3.1))
print(math.floor(3.9))
#3
numbers = [-5, 2.7, 10, -3]
print(min(numbers))      # -5
print(max(numbers))      # 10
print(abs(-7))           # 7
print(round(3.6))        # 4
print(pow(2, 3))         # 8
#4
import math
print(math.sqrt(16))     # 4.0
print(math.ceil(4.2))    # 5
print(math.floor(4.9))   # 4
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))       # 1.0
print(math.pi)           # 3.141592653589793
print(math.e)            # 2.718281828459045
#5
import random
nums = [1, 2, 3, 4, 5]
print(random.random())      # число от 0 до 1
print(random.randint(1, 10))# целое число
print(random.choice(nums)) # случайный элемент
random.shuffle(nums)        # перемешивает список
print(nums)