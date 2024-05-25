# open the file (read r),(write w),(append a).....
f=open("shanzy.txt","r")
text=f.read()
print(text)
f.close()
#  write mode (if file not exist it create).......
f= open("shanzy1.txt" , 'w')
print("hello am shanzy")
# append mode (add somethig to already existig file)
f=open("shanzy1.txt","a")
# f.write("shsjsksk")
print("chal nikal")
# create mode 
"""f=open("shanza.txt","x")
print(f)"""
# text it can open file in text mode
f=open("shanzy.txt","rt")
print(f)
# binary it can open file in binary mode(images,pdf)
f=open("shanzy.txt","rb")
print(f)
with open("shanzy.txt" , "a") as f:
    f.write("sjskskakl")
    
