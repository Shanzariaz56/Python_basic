a="shanza!!!!" #single line string
b="""shanza is a good girl 
welcome to our website""" #multiple line string
print(a)
print(b)

#slicing string..........
a="shanzaa"
print(a)
print(len(a))
print(a[0])  #index wise show character
print(a[1])
print(a[1])
print(a[2])
print(a[3])
# also access by for loop like
for i in a:
    print(i)
# more slicing string..............
a="mangoess"
print("length of mango is:",len(a))
print(a[2:6])
print(a[0:7])
print(a[-4:-1]) # we can chk it by len(a)-index like 7-4=3(start with 3)
print(a[-6:-4])   
print(a[-5:-1])

#method of string.............
a="shanza riaz !!!!!"
b="welcome to my website"
print(a.upper())
print(a.lower())
print(a.isupper())
print(a.islower())
print(a.swapcase())
print(a.center(50))
print(b.istitle())
print(a.isalpha())
print(a.isalnum())
print(a.find("shanza"))
print(b.index("to"))
print(b.capitalize())
print(a.rstrip())
print(a.replace("shanza","shanzy"))
print(a.split())



