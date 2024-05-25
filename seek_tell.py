with open("shanzy.txt","r") as f:
    f.seek(10)   # it move to the 10 position
    data=f.read(5)  # after 10 positon it read the next 5 character and print it
    print(data)
# "tell()" it can tell the current location of the seek point....
with open("shanzy.txt","r") as f:
    f.seek(9)
    print(f.tell())
    d=f.read(3)
    print(d)
# "trauncate()" can be used to fix the size of the file
with open("shanzy.txt" , "w") as f:
    f.write("shanzyy khan")
    f.truncate(5)
with open("shanzy.txt","r") as f:
    print(f.read())

