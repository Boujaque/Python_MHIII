# 3  - working with directories
from pprint import pprint as print
from pathlib import Path

path = Path("Chapter8_Modules\ecommerce")

print(path.exists())
# path.mkdir()
print(path.exists())
# path.rename("ecomerce2")
print(path.exists())
# path.rmdir()

print(path.iterdir())
for p in path.iterdir():
    print(p)
# using list comprehension:
paths = [p for p in path.iterdir()]
print(paths)

# applying filter on compr. list
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# there are two limitations:
# cannot be searched by patern
# cannot be searched recursively
# glob() method
path.glob("*.*")  # return object generator
path.glob("*.py")  # return object generator
print("Glob method")
py_files = [p for p in path.glob("*.py")]
print(py_files)
# searching recursively
print("py files:")
py_files = [p for p in path.glob("**/*.py")]
print(py_files)
