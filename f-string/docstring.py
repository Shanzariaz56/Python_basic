#firstly formatting string is  used in python to format the text
a="my name is {} and i am belong to {}"
name="shanza"
country="pakistan"
print(a.format(name,country))
#now we can use f-string for formatting
print(f"my name is {name} and i am belong to {country}")
#another example of f-string will be 
price=890
print(f"the price of shirt will be {price}")
#doc string and pep-8.............................................
#like we have a function and the doc string can be wite after the function.....
def square(n):
    '''take a number n , and return the sqyare of the number'''
    print(n**2)
square(5)
#print the doc string will be like.....
print(square.__doc__)
#another function will be....
def add(a,b):
    '''it can take two number and return the addition of that number'''
    c=a+b
    print(c)
add(12,8)
print(add.__doc__)
#PEP (python enhancement proposal) improve readability etc.....
#pep is zen in python 