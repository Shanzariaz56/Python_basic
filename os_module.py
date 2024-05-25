# to make a multiple folder at onces use "mkdir"
# "os module" can ce used to make a file at folder read/write/open a file
import os
#condition is apply bcz data folder is already exsit so to save the error
if(not os.path.exists("data")):
 os.mkdir("data")                   # it show error that folder is already exist if you want to print it again

for i in range(0 ,10):
    os.mkdir(f"data/day{i+1}")
# if we want to rename the file name so..........
for i in range(0 ,10):
   os.rename(f"data/day{i+1}", f"data/turtorial {i+1}")
# if you want to check how many folder is exist "listdir"
folders=os.listdir("data")
print(folders)
# if you want to pirnt it in a sequence
for folder in folders:
 print(folder)
 # if you want ot check a folder inside th folder
for folder in folders:
  print(os.listdir(f"data/{folder}"))
os.remove("data")