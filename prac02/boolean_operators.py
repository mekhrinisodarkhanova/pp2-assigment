#1
a = 45
b = 34 
c = (a>50) and (b==34)
print(c)
#2
a = "banana"
b = "apple"
c = (a=="apple") or (b=="banana")
print(c)
#3
a = True
b = False
c = True 
d = (a and c) and (a or b) or not(c)
print(d)  
#4
a = 0
b = 10
if a!=6 and (a/10 > -5):
    print(True)
#5
a = ["apple", "banana"]
if len(a)>9:
    print(f"{len(a)} greater then 9")
else:
    print(f"{len(a)} less then 9")