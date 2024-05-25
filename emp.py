class employee:
    def __init__(self,n):
        self.name = n
# __len__ method that retur the length of the object..........................................................
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
# __str__ method...............................................................................................
    def __str__(self):
        return f"this is the string method and the Name of the employee will be {self.name}"
    
# __repr__ method is used to recreate that object...............................................................
    def __repr__(self):
        return f"employee('{self.name}')"
    
# __call__ method is used to call the object of the call as function
    def __call__(self):
      print("shanza")