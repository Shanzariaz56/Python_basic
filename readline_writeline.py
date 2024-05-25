# if you print lines before the condition so it can not take extra space that is string
f=open("student_arks.txt","r")
while True:
    lines=f.readline()
    if not lines:
        break
    print(lines)
# if lines is print before the condition so it take acn extra string at the end
while True:
    lines=f.readline()
    print(lines)
    if not lines:
        break   
# if you take student marks like;(readline method0)
f=open("student_arks.txt","r")
i=0
while True:
    i=i+1
    lines=f.readline()
    if not lines:
        break
    m1=lines.split(",")[0]
    m2=lines.split(",")[1]
    m3=lines.split(",")[2]
    m4=lines.split(",")[3]
    print(f"marks of student {i} in English {m1}")
    print(f"marks of student {i} in Urdu {m2}")
    print(f"marks pf student {i} in DLD {m3}")
    print(f"marks of student {i} in Math {m4}")
# writelines method .................................................
f=open("shanzy1.txt","w")
lines=["line1\n ,line2\n,line3"]
f.writelines(lines)
f.close()
# if you print huge list.....
f=open("shanzy1.txt","w")
lines=["line1,line2,line3"]
for line in lines:
    f.write(line +"\n")
f.close()
    