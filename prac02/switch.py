#1
x = int(input())
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
#2
score = int(input())
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")
#3
day = int(input())
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Weekend")
#4
age = int(input())
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
#5
a = int(input())
b = int(input())
op = input()
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Unknown operation")