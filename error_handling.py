#server error occur like we can't define datatype so we can
n=input("enter the number")
print(f"the multiplication table {n}")
for i  in range(1,11):
    print(f"{int(n)} X {i} = {int(n)*i}")
# we can use try/except if there is error so except statement is excute
n=input("enter the number")
try:
    for i in range(1,11):
        print(f"{int(n)} X {i} = {int(n)*i}")
except:
    print("error occur")
print("shanzy _khan7")
#we can use multiple except....
try:
    a=int(input("enter the number"))
    n=[5,6]
    print(n[a])
except ValueError:   #it can handle the error occure due to the wrong value
    print("you should enter the wrong value")
except IndexError:   #it can handle the error when you gave the wrong index
    print("wrong index value")
#use a finally keyword after except and statment inside must excute
try:
    l=[1,2,2,3,4,5]
    i=int(input("enter the index:"))
    print(l[i])
except:
    print("eroor occur")
finally:       #always excuted
    print("it will always excuted")
# in case of function it will excute always even it return value
def func():
    try:
        l=[1,2,3,4,5,6]
        n=int(input("enter the number"))
        print(l[n])
        return 1
    except:
        print("eror occur")
        return 0
    finally:
        print("this statement will always excuted")
x=func()
print(x)
        
