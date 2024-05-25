class person:
    def __init__(self,n,a,w) :    # initialozation of the constructor and pass arguments (self argument is pass as an object of class)
        print("consturctor cal when object of the class is created")
        self.name=n
        self.age=a
        self.weight=w

    def info(self):  # function ,.......
        print(f"my name is {self.name} my age is {self.age} nd my weight is {self.weight}")
# create the object of the class..................
p1=person("shanza",20,50)
p2=person("saira",19,52)
p1.info()
p2.info()

# by default constructor is call.....
class student:
    name="shanza"
    age=19
    def __init__(self) :
       print("automatically class")
    def info(self):
        print(f"name is {self.name} and age {self.age}")
s1=student()
s1.info()
s2=student()
s2.info()
