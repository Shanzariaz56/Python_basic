# static method belong to the class rather then the instance of the class
# never need to acess the instance and class method(self)
class math:
    def __init__(self,n1) :
        self.num=n1
    def add_num(self,n2):
        self.num=self.num+n2
    @staticmethod
    def add(a,b):
        return a+b
a=math(9)
print(a.num)
a.add_num(6)
print(a.num)
# static method can be call by instance and also by class name
print(a.add(1,3))
print(math.add(5,6))
