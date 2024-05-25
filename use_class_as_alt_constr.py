class s:
    def __init__(self,n,age,add):
        self.name=n
        self.age=age
        self.address=add
# class method decorator can be used as the alternative of the constructor..................................................
    @classmethod
    def string(cls,str):
        return cls(str.split("-")[0],int(str.split("-")[1]),str.split("-")[2])
    def show(self):
        print(f"name is {self.name} and him age {self.age} and birth place is {self.address}")

s1=s("sairo",19,"multan")
s1.show()
print(s1.name)
print(s1.age)
print(s1.address)

# if we want to take a string and from that string we will pick the name and salary..........................................
 # split it by ("-") then it convert it into list............................................................................
str="shanza-20-vehari"
s2=s(str.split("-")[0],str.split("-")[1],str.split("-")[2])    # by using thius we can make a class method by this...........
print(s2.name)
print(s2.age)
print(s2.address)

# class method...............................................................................................................
s3=s.string(str)
print(s3.name)
print(s3.age)
print(s3.address)
