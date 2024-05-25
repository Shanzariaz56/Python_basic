#even/odd
num=int(input("enter a number"))
if(num%2==0):
    print("even number")
else:
    print("odd number")
a=int(input("enter your age"))
print(a)
#conditional operators
#(>,<,<=,>=,==,!=)
#print(a>=18)
#print(a<=18)
#print(a==18)
#print(a!=18)
#print(a<18)
if(a>18):
    print("you can get driving licese")
else:
    print("can't drive")
# if elif else statement like
# find the largest number....................
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
d=int(input("enter the 4th number"))
if(a>b and a>c and a>d):
    print("the largest number will be a:",a)
elif(b>a and b>c and b>d):
    print("the largest number will be b:" ,b)
elif(c>a and c>b and c>d):
    print("the largest number will be c:",c)
else:
    print("the largest number will be d:",d)

# find the smallest number...................................
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
d=int(input("enter the 4th number"))
if(a<b and a<c and a<d):
    print("the smallest number will be a:",a)
elif(b<a and b<c and b<d):
    print("the smallest number will be b:" ,b)
elif(c<a and c<b and c<d):
    print("the smallest number will be c:",c)
else:
    print("the smallest number will be d:",d)
