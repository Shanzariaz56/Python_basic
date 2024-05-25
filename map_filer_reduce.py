# make a cube function...................
def cube(x):
    return x*x*x
print(cube(2))
# make a list............................
l=[1,2,3,4,8,7,6]
newl=[]
for i in l:
    newl.append(cube(i))
print(newl)
# map function can be applied to a function each element in a sequence and return a new sequence containing the transformed element.........
l1=[1,3,8,9,6,5,4]
newll=list(map(cube,l1))
print(newll)
# alos use a lambda function.......
l=[1,2,3,4,5,6]
newl=list(map(lambda x:x*x*x,l))
print(newl)
# filter function.........................
def filtr_func(a):
    return a>2
newl1=list(filter(filtr_func,l1))   # lambda a: a%2==0
print(newl1)
# reduce it can reduce the list and it can be import....
from functools import reduce
l3=[1,2,3,4,5,6,7]
sum=reduce(lambda x,y :x+y,l3)
print(sum)
