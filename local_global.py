# global variable can be inside the function if the sa,e number variable is not exist in the function
x=10
print(x)
def shanza():
    # we can chnage value of global varavile by using "global" keyword
    global x
    x=3
    x=5
    y=20
    print(f"the local varaible {x}")
    print(f"the local varaible {y}")
# function call...
shanza()
print(f"the gobal variable {x}")