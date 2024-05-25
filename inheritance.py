class student:
    def __init__(self,n,a,m):
        self.name= n
        self.age= a
        self.marks= m
    def show_detail(self):
        print(f"my name {self.name} my age {self.age} and i have score marks {self.marks}")

# now make the dervied class and join it to the base class......

class student_field(student):
     def field(self):
          print("the field that i was choose will be computer")

s1=student("shanza",19,100)
s1.show_detail()
s2=student_field("saira",20,200)
s2.show_detail()
s2.field()
s3=student_field()
s3.show_detail()