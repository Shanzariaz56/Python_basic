# "is" can compare the exact loaction of object in the memoery
# "==" can compare the value of the oject
a=2
b=2   # "2 " is constant so it take exaclty one place in memory
print(a is b)
print(a==b)
# aonther example 
a="4"
b=4
print(a is b)
print(a==b)
# another example list is mmutable 
a=[1,2,3]
b=[1,2,3]
print(a is b)   #bcz it is changable so both "a and b" point own list not same
print(a==b)
# another example..........
a=(1,2)
b=(1,2)
print(a is b)
print(a==b)