# import work like....
"""import pandas
pandas.read_csv()"""
# another module is import......
import math 
result=math.sqrt(9)
print(result)
# "from" keyword is use in import.....
from math import sqrt , pi
res=sqrt(9)*pi
print(res)
# also see "*" at some place it means all the function of module is import
from math import *
print(type(math.modf))
# "as"  keyword is use for a short cut like....
import math as m
result=m.pi*2
print(result)
#another example of import will be like....
from math import sqrt as s
res=s(9)
print(res)
# "dir" keyword is use to check how many function is reside in the module........
import math 
print(dir(math))
# anthor example make module by yourslef like....
from shanza import addition , a
addition()
print(a)
