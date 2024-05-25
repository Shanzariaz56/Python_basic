def wellcome():
    print("welcome to the shanzy store")
# now, print the name to check that it is run at that module
print(__name__)   # it print __main__ it means it is run at there
  
 # check to avoid problem when you import a module so it cant excute it
if __name__=="__main__": 
  wellcome()