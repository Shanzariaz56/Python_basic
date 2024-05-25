a=int(input("enter the number"))
while(a<=38):
    a=int(input("enter the number"))
    print(a)
    a=a+1
print("loop end")
#anpther example.................. even number print
a=int(input("enter a number"))
while(a<50):
    if(a%2==0):
        print(a)
    a=a+1
#break statement............. it terminate loop
a=int(input("enter the number"))
for i in range(1,12):
    if(i==10):
        print("loop terminate")
        break
    print(a,"x",i,a*i)
#continue statement............... it terminate iteration
a=int(input("enter the number"))
for i in range(1,12):
    if(i==10):
        print("iteraation skip")
        continue
    print(a,"x",i,a*i)
