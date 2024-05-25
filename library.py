class library:
    def __init__(self):
        self.b_name=[]
        self.b_no=0
    def add_books(self,books):
        self.b_name.append(books)
        self.b_no=len(self.b_name)
    def show(self):
        print(f"No of book will be {self.b_no}: Name of book will be {self.b_name}")
        for i in self.b_name:
            print(i)
l1=library()
l1.add_books("URDU")
l1.add_books("english")
l1.add_books("physics")
l1.add_books("dld")
l1.add_books("maths")

l1.show()