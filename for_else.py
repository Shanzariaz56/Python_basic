#else is used with the for loop 
for i in range(6):
    print(i)
    if(i==4):
        break
else:
    print("statement break")  # it can't execute bcz of the break statment

#anthoer example
i=0
while i<7:
    print(i)
    i=i+1
else:
    print("loop end")
#format case....
for i in range(6):
    print("the iteration no {} in the loop".format(i+1))
else:
    print("end")