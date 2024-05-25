import shanza
shanza.wellcome()
# here problem is that when you import module shanza so all the function inside it is automatically excute 
# so, to avoid this problem we can use __name__="__main__"