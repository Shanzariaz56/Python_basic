s={"name":"shanza","age":"19"}
print(s)
#element/value of dic can de access like(single key)
print(s["name"])
# for multiple keys use (key) word like
print(s.keys())
# print values crossponding key use for loop
for i in s.keys():
    print(s[i])
# written in the pair form
print(s.items())
#in the form of for loop
for key,values in  s.items():
    print(f"the key {key} and the value{values}")
#another example of dictionery...
s1={
    "name":"shanza",
    "age":20,
    "gpa":3.86
}
s2={
    "name":"saira",
    "age":21,
    "gpa":3.71
}
s3={
    "name":"saira",
    "age":22,
    "gpa":3.61
}
students={
    "s1":s1,
    "s2":s2,
    "s3":s3
}
# method of dictionary.....
#update method....
c1={
    1:1092,2:990,3:690,4:987,5:1020
}
c2={8:1056,9:456,10:789}
c1.update(c2)
print(c1)
#clear method..
c1.clear()
print(c1)
#pop method
c1.pop(3)
print(c1)
#pop item method it ca remove last element
c1.popitem()
print(c1)
#del method...
del c1
print(c1)
