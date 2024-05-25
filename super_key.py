# super key can be used to inherit the child class from the multiple parent class...............................
class parent:
    def parent_method(self):
        print("this is the parent class")

class child(parent):
    def parent_method(self):
        print("shanzyyyyyy")
        super().parent_method()
    def child_method(self):
        print("this is the child class")
        super().parent_method()   # it can call all the method of the parent class..............................

c=child()
c.child_method()
c.parent_method()

# another example................................................................................................
class employee:
    def __init__(self,n,a,id):
        self.name=n
        self.age=a
        self.id=id
    def parent(self):
        print("this is the parent class")

class programmer(employee):
    def __init__(self,n,a,id,lang):
        super().__init__(n,a,id)
        self.language=lang

e=employee("saira",19,450)
p=programmer("shanzy",20,130,"python")
print(p.name)
print(p.age)
print(p.id)
print(p.language)

        
