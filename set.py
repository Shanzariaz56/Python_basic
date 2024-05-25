#set cannot print repeated values
s={"shanza",9,9.8,False,9}
print(s)
print(type(s))
# empty set can never be written like this bcz dic and set are start with curly braces
s1={}
print(type(s1))
# empty set can be written as
s2= set()
print(type(s2))
# using for loo[ in set
for i in s:
    print(i)
    if(i=="shanza"):  # print element in shanza
        for j in i:
            print(j)
#method of the list........
#1-union method
s1={1,2,9,7,8,4,2}
s2={1,5,3,0,11,9,8}
s3=s1.union(s2)
print(s3)
#union_update method......
s1={1,2,3,4.5}
s2={2,4,7,8,9}
s1.update(s2)
print(s1)
#intersection method
s1={1,2,3,4,5,6}
s2={2,4,5,9,0,7}
s3=s1.intersection(s2)
print(s3)
#intersection_update method
s1={1,2,3,4,5}
s2={2,3,7,8,9}
s1.intersection_update(s2)
print(s1)
#symmetric method(it the print the value that is not common and skip the common values)
s1={1,2,3,4,5}
s2={2,3,6,7,8}
s3=s1.symmetric_difference(s2)
print(s3)
#different method(skip the elements that is common in s2)
s1={1,2,3,4,5}
s2={2,3,6,7,9}
s3=s1.difference(s2)
print(s3)
#difference_update method
s1={1,2,3,4,5}
s2={2,4,8,9,6}
s2.difference_update(s1)
print(s2)
#add method
s1={1,2,3,4,5}
s1.add(6)
print(s1)
#isdisjoint method(check bth set if any one element is match so it print false)
s1={1,2,3,4,5,6}
s2={2,3,6,7,8,9}
s3=s1.isdisjoint(s2)
print(s3)
#issubset method(check that all the element are exist in the set)
s1={1,2,3,4,5,6,7}
s2={2,4,5,6,7}
s3=s2.issubset(s1)
print(s3)
#issuperset method
s1={1,2,3,3,4,5,6}
s2={3,4,6}
s3=s1.issuperset(s2)
print(s3)
#remove method
s1={1,2,3,5,6,7}
s2={2,3,4,5,99}
del s2
print(s2)
#pop method(random pop any element)
s1={1,2,3,4,5,66}
s1.pop()
print(s1)
#clear method..
s1={1,2,3,4,5}
s2={2334,4,5,6}
s1.clear
print(S1)