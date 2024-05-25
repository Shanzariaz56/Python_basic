class employee:
    company_name="apple"    # class variable......
    employee_no=0
    def __init__(self,n):
        self.name= n
        self.age=19   # instance variable asssoicated with the instance
        employee.employee_no += 1
    def show(self):
        print(f"the name of the employee {self.name} and the age {self.age} and in {self.employee_no} working in company {self.company_name}")
e1=employee("shanza")
# change the instance varaible
e1.age=20
e1.company_name="nestle"   # change the class variable
e1.show()
e2=employee("ahmad")
e2.show()