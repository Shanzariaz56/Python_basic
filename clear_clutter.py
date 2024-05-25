import os
class clear:
    def cluterr(self):
        if(not os.path.exists("files")):
            os.mkdir("files")
        for i in range(0,5):
            os.mkdir(f"files/shsjsksks {i+1}")
    def rename(self):
        for i in range(0,5):
            os.rename(f"files/shsjsksks {i+1}",f"files/{i+1}.png")
c=clear()
c.cluterr()
c.rename()