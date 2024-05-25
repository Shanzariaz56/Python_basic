def meancal(a,b):   #function to calculate mean
    mean=(a+b)/(a*b)
    print(mean)
def largest(a,b,c): #function to find the largest  number
    if(a>b and a>c):
        print("the largest number will be a:",a)
    elif(b>a and b>c):
        print("the largest number will be b:",b)
    else:
        print("largest number will be c:",c)
def smallest(a,b,c): #function to find the smallest number
    if(a<b and a<c):
        print("the smallest number will be a:",a)
    elif(b<a and b<c):
        print("the smalllest number will be b:",b)
    else:
        print("largest number will be c:",c)
#using function in the program
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
meancal(a,b)
largest(a,b,c)
smallest(a,b,c)
#using function in other statements same function
c=int(input("enter the number"))
d=int(input("enter the number"))
e=int(input("enter the number"))
meancal(c,d)
largest(c,d,e)
smallest(c,d,e)


'''function is for the addition
def adding(a,b):
    c=a+b
    print(c)
def subtarction(a,b):
    c=a+b
    print(c)
def calculatemean(a,b):
    c=(a+b)/(a*b)
    print(c)
print("press 1 for addition\n")
print("press 2 for subtraction\n")
print("press 3 for geomeric mean\n")
a=int(input("enter your choice"))
print(a)
match a:
    case "addition":
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        adding(a,b)
    case "sub":
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        subtarction(a,b)
    case "mean":
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        calculatemean(a,b)
    case _:
        print("invalid")'''
