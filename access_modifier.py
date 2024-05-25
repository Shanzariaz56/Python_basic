# public modifier (by default).............................................................................
class employee:
    def __init__(self):
        self.name= "shanza"
        self.address= "multan"
    
e=employee()
print(e.name)
print(e.address)

# private modifier( use double underscore with the variable name)..........................................
class student:
    def __init__(self) :
        self.__marks = 900   #( now it is private variable)................................................
        self.__course = "cs"

s=student()
print(s._student__marks)    # it can be access by class name...............................................
print(s._student__course)

# dir( function) can check that how many function is apply on the class object.............................
print(s.__dir__())

# name mangling............................................................................................
class std:
    def __init__(self) :
        self._private_att="private will be here"
        self.__mangling_att="mangling attribute is here"

obj=std()
print(obj._private_att)   #simply print the output........................................................
#print(obj.__mangling_att) # error throw bcz it is private................................................
print(obj._std__mangling_att)

# another example........................................................................................
def shanza():
    def __init__(self,n,a):
        self.__name = n
        self.__age = a
    def __show(self):
        self.y=2003
        print(self.y)    

ob=shanza("shanza",19)   # error  throw
print(ob.__age)    # error
print(ob.__show)   # error

# protected access modifier...............................................................................
class pro:
    def __init__(self):
        self._name= "shanza"
        self._uni = "comsats"
    def _func(self):
        print("not so easy")
class protect(pro):
    pass
p=pro()
p1=protect()
print(p._name)
print(p._func())
print(p._uni)
print(p1._func())
print(p1._uni)


