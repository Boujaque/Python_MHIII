# 2 Working with paths
from pathlib import Path

# \ is escape character need to be doubled
Path("C:\\Program Files\\Microsoft")
Path(r"C:\Program Files\Microsft")  # using raw strings  no ned to double \\
# For linux
Path("/usr/local/bin")
Path(r"C:\SoftDev\Mosh_Python\VS_Code\Chapter8_Modules\ecommerce\shopping\sales.py")
Path(r"Chapter8_Modules\ecommerce\shopping\sales.py")

print(Path.home())  # home directory of the user:  C:\Users\rafae
# Check objects of the pathlib on google
path = Path(r"Chapter8_Modules\ecommerce\__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)  # File name
print(path.stem)  # filename without extension
print(path.suffix)  # file extension/ suffix
# print(path.parrent)  # file extensio?n/ suffix
path = path.with_name("file.txt")
print(path)
print(path.absolute())
path = path.with_suffix(".py")
print(path.absolute())
