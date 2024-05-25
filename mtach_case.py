a=int(input("enter your choice"))
print("press 1 for the addition\n")
print("press 2 for the subtraction\n")
print("press 3 for the multiplication\n")
print("press 4 for the division\n")
match a:
    case 1:
        a=int(input("enter 1st number"))
        b=int(input("enter 2nd number"))
        c=a+b
        print("result of addition will be:",c)
    case 2:
        a=int(input("enter 1st number"))
        b=int(input("enter 2nd number"))
        c=a-b
        print("result of subtaction will be:",c)
    case 3:
        a=int(input("enter 1st number"))
        b=int(input("enter 2nd number"))
        c=a*b
        print("result of multiplication will be:",c)
    case 4:
        a=int(input("enter 1st number"))
        b=int(input("enter 2nd number"))
        c=a+b
        print("result of addition will be:",c)
    case _:
        print("invalid case")
        
# another example of match case is that............
response_code=404
match response_code:
    case 400:
        print("server cant understand")
    case 401 |403:
        print("server cannot access")
    case 404:
        print("server cant find")


