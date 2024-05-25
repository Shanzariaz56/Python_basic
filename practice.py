class parent:
    def __init__(self,x,y):
        self.x= x
        self.y= y
    def area(self):
        return self.x*self.y
    def show(self):
        print("the area will be show as")
class child(parent):
    def __init__(self,r):
        self.radius= r
        super().__init__(r,r)
    def area(self):
        return 3.14 * super().area()
    
c=child(8)
print(c.area())

