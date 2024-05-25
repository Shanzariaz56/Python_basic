#simply print a list
list1=[28,25,78,67,98,65,43,87,69]
list2=[1,"shanza",100,3,"shanzyyy",True,9,3.9,8,"saira"]
print(list1)
print(list2) 
#slicing the list will be like
print(list1[0])
print(list1[1])
print(list1[2])
print(list2[1])
#another example of slicing
print(list2[3])
print(list2[0:4])
print(list2[4:7]) # positive slicing
print(list2[-6:-2])  #negative slicing
print(list2[1:9:2])
#using for loop in the list.....
for i in list1:
    print(i)
#using if in list.......
if 25 in list1:
    print("yes")
else:
    print("no")
#another way in string case....
if "shanzaa" in list2:
    print("Yes")
else:
    print("No")
#list of comprehension.............
# syntax will be like; newlist=[expression(item) for item in iterated if condition==true]
#simple print a list i range 6
list=[i for i in range(6)]
print(list)
#print a list of only even number will be like
list=[i for i in range(20) if i%2==0]
print(list)
#print a list like....
list2=[i*i for i in range(20) if(i%2==0)]
print(list2)
#print a list of new items like....
list1=["shanza","saira","mehwish","talha","ali","iqrrrr"]
newlist=[i for i in list1 if "a" in i]
print(newlist)
#method of list.........
# l.append()
# l.insert(index,item)
# l.sort() ascending
# l.sort(reverse==true) descending
# l.reverse()
# l.copy()
# l.extend(new_list)
# l.index(item)
# l.count(item)
l=[1,2,56,9,8,76,4,56,87,90,90,1,3,2]
print(len(l)) 
# append method in list.....
l.append(100)
print(l)
# sort method in list ascending
l.sort()
print(l)
# sort method in list descending
l.sort(reverse=True)
print(l)
# reverse method in list 
l.reverse()
print(l)
# index method of list...
l.index(4)
print(l)
# copy the list 
m=l.copy()
print(m)
# insert method in list
l.insert(3,120)
print(l)
# extend method of list
m=[100,890,900,789,678]
l.extend(m)
print(l)
# remove list iyem
l.remove(100)
print(l)
# remove like
l.pop(3)
print(l)