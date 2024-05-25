#tuple can never be change once the data is enter into it
tuple=(1,2,3,4,"shanza","vehari",True,"saira",9)
print(tuple)
#length of the tuple.....
tup=len(tuple)
print(tup)
#index wise print the tuple...
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple[-1])
#also use the for loop in tuple
for i in tuple:
    print(i)
#if statment can aslo be use like
if "shanza" in tuple:
    print("yes it is presnt")
else:
    print("not present")
#slicing of the tuple will be like......
print(tuple[0:4])
print(tuple[1:6])
print(tuple[-5:-3])
print(tuple[-6:-1])
print(tuple[:5])
#operation in tuple......
#tuple can never change so first we can conevr it into the list and then after changing the list will be again tuple
tup=("shanza","saira","ahmad","abdullah","hira","ayesha","riaz","talha")
temp=list(tup)
temp.append("shanzyy")
temp.pop(5)
temp[2]="ali"
tup=tuple(temp)
print(tup)
#method of tuple directly apply......
#index(element,start,end)
#count(element)
tuple=(1,2,3,4,5,6,2,3,3,3,3,2,1,4,5,3,6)
tup=tuple.count(3)
print(tup)
#index method
tup=tuple.index(3)  #it show the starting index where the 3 is present first
print(tup)
#another way of indexing will be like 
#index(element,start,end)
tup=tuple.index(3,4,8)
print(tup)