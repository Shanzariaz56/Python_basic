class student:
    uni_name="comsats"
    uni_campus="vehari"
    def __init__(self,n,a):
        self.name= n
        self.age= a
    def show(self):
        print(f"name is {self.name} and age is {self.age} and study in azab {self.uni_name} university campus {self.uni_campus} ")

# now here we want to change the variable/instance of the class so we cam use the class method 
# use a decorator that can take first argument of the function as the class an change directly the variable of the class for the whole class  
  
    @classmethod
    def change_class(cls,chg_uni_n,chg_cmp):
        cls.uni_name= chg_uni_n
        cls.uni_campus= chg_cmp

s1=student("shanza",20)
s1.uni_campus="sargoda"
s1.show()

# after change the class variable ..................
s1.change_class("iqra","karachi")
s2=student("ahmad",21)
s2.show()  
# now the variable of classs.....
print(student.uni_campus)