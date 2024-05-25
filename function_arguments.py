# default arguments........
def adding(a=10, b=30):
    c = a+b
    print(c)
# another function..........


def list(fname, lastname="riaz", country="pakistan"):
    print(fname, lastname, country)


# take a value.......
a = 10
b = 5
adding(a, b)
# not gave a value so it take it by default
adding()
# gave one value second will be dafult
adding(5)

# another exammple of default arguments are.................
fname = "shanza"
list(fname)
# required arguments.......
fname = "shanzyyy"
lastname="khan"
list(fname,lastname)
#variable_length argument......
#if i want to find a average of some number so we take a for loop like
def average(*number): #*number means it take multiple number
        sum=0
        for i in number:
             sum=sum+i
             average=sum/len(number)
             print("total average :",average)

#calling the above function
average(5,1,6,10)