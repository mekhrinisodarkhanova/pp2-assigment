#1
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
#2
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#3
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
#4
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1
ctr = fun(5)
for n in ctr:
    print(n)
#5
sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)