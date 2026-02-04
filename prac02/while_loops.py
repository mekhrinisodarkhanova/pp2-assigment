#1
i = 1
while i < 6:
  print(i)
  i += 1
#2
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#3
n = int(input())
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)
#4
password = "1234"
user_input = ""
while user_input != password:
    user_input = input("Enter password: ")
print("Access granted")
#5
n = int(input())
i = 0
min_value = 10**9
while i < n:
    x = int(input())
    if x < min_value:
        min_value = x
    i += 1
print(min_value)