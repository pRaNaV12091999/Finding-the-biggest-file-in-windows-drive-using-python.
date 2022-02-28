import glob
from importlib.metadata import files
from importlib.resources import path
import os
dirname = "D:\\"
print("Current working directory",os.getcwd())
os.chdir(dirname)
print("New working directory",os.getcwd())
listoffiles=glob.glob(dirname+'*/**/*',recursive=True)
# # print(listoffiles)
maxfile=max(listoffiles,key=lambda x:os.stat(x).st_size)
maxsize=os.stat(maxfile).st_size
print("Name of the biggest file:",maxfile, "Its size is :",maxsize)

