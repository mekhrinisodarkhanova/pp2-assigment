#1
print(10 > 9)
print(10 == 9)
print(10 < 9)
#2
bool(False)
bool(None)
bool(0)
bool("")
bool(())
#3
bool(True)
bool(1)
bool("abc")
bool(123)
#4
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
#5
x = 200
print(isinstance(x, int)) 
#проверяет, является ли объект экземпляром определенного класса или его подкласса