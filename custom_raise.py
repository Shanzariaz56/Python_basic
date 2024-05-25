#custom error ...
a=int(input("enter the value between 6 ansd 10:"))
if(a<6 or a>10):
    raise("here is the error10")
# anothr example ......
n=input("ener the string:")
if(n=="quite"):
    print("you are right")
else:
    if(int(n)<5 or int(n)>9):
        raise("error")
