# list .............................................................................
x=[1,2,3,4,5,6]
print(dir(x))   # it can show the detail that how many method we can use for the list
print(x.__add__)

# tuple..............................................................................
y=(3,4,5,6,6,7)
print(dir(y))

# __dir__ method that represent the object of he class as a dictionary...............
class s:
    def __init__(self,n,age,add,m):
        self.name=n
        self.age=age
        self.address=add
        self.marks=m
    
s1=s("shanza",20,"vehari",1092)
print(s1.__dict__)

# help function is used to get the help documentation of the object..................
print(help(s1))