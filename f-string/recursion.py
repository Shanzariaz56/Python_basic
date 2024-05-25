#in case of the recursion we can use the function inside the function
# like we can write the function of calculatin factorial as
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)  
n=int(input("enter the number"))
print(n)
print(factorial(n))
#fibonicca series......
#f0=0 , f1=1 , f2= f1+f0=1 fn=f(n-2) +f(n-1)
#function will be 
def fib(n):
    if(n==1 and n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter the number"))
print(n)
fib(n)        