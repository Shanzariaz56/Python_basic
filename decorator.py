# take a function return a new function that modify the original function
def greet(func):   #make a function and pass function as arugment
   def n_func():
      print("welcome to this store")
      func()
      print("that was a good store")
   return n_func

# wuthout an argument..........   
@greet   
def add():
     print("sum of two values : 9")
add()
# with an arugument.......
def decorate(function):
    def modify_func(*args,**kwargs):  # *args consider the arguments as a  tuple , **kwargs consider the arguments as dictionary
        print("good morning")
        function(*args,**kwargs)
        print("thank you")
    return modify_func
@decorate
def sum(a,b):
    print(a+b)

sum(1,4)
    