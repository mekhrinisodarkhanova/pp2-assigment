#1
while True:
    x = int(input())
    if x == 0:
        break
    print(x)
#2
while True:
    x = int(input())
    if x < 0:
        break
#3
secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct!")
        break
#4
total = 0
while True:
    x = int(input())
    if x < 0:
        break
    total += x
print(total)
#5
password = "admin"
attempts = 0
while True:
    user = input()
    attempts += 1
    if user == password or attempts == 3:
        break