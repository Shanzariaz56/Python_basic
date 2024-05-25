# make a class and then define its object..........
class student:
    name="shanza"
    age=20
    address="vehari"
    def info(self):
        print(f"my name is {self.name} and am {self.age} years old and am living in {self.address}")
        
s1=student()
s2=student()
s3=student()
 
s1.name="shanzy"
s1.age=19
s1.address="multan"

s2.name="saira"
s2.age=18
s2.address="lahore"

s1.info()
s2.info()
s3.info()