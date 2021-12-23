# 4 Working with Files
from pathlib import Path
from time import ctime
import shutil

path = Path(r"..\Chapter8_Modules\ecommerce\__init__.py")  # for pycharm
print("Status:", path.stat())
print("Ctime Status:", ctime(path.stat().st_ctime))
print(path.exists())

# path.rename("init.txt")
# print(path.exists())

# Reading data from a file
# print(path.read_byt())
# return the context of the file as a string
path = Path(r"..\Chapter7_Classes\app7.11.py")
print(path.read_text())
# this replace the method of reading a file:
# with open("__init__.py","r") as file:
#     pass
#Method for writing text or bytes:
path.write_text("...")
path.write_bytes()
# for coppying  files path is not the optimum

source = Path(r"..\Chapter7_Classes\app7.11.py")
target = Path()/"..\\ecommerce"
target.write_text(source.read_text())

# better way is to use shutil
shutil.copy(source, target)
target.write_text(source.read_text())