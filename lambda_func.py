# lambda function..........(anonympus function that has no name but it is expression)
def sum(a,b):
    return a+b
print(sum(5,6))
# another example............
def func(cube,value):
  return cube(value) +6
#print(func(cube,2))
# as compare to write a function we can write it as:......
sum=lambda a,b: a+b
print(sum(1,2))
# another example......
cube= lambda x: x*x*x
print(cube(9))
# another example will be(use function inside a function).....
print(func(lambda x : x*x*x,6))
print(cube(3))
# another example......
avg=lambda x,y,z : (x+y+z)/3
print(avg(1,2,3))