#it can also print the index with the value
#without enumerate function...
list=["shanza",1,2,3,4,5,88,66,44,55,66,77,33]
index=0
for marks in list:
    print(marks)
    if(index==4):
        print("good marks")
    index=index+1
# with the enumerate function.....
list=[22,33,55,67,55,44,89,77,67,56,89,33]
for index,marks in enumerate(list):
    print(marks)
    if(index==6):
        print("goood")
# can also print the index with that like.....
list=[22,44,55,66,77,88,99,22,45,6,78,45,34]
for index,marks in enumerate(list):
    print(index,marks)
# you can also gave the start of the index
list=[11,22,33,55,66,77,88,99,44,33,33,55,667,789]
for index,marks in enumerate(list,start=1):
    print(index,marks)