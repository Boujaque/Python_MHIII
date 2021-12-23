# 5 - Working with zip Files
from pathlib import Path
from zipfile import ZipFile

# zipFile = ZipFile("files.zip","w")
# for path in Path(r"..\Chapter8_Modules\ecommerce").rglob("*.*"):
#     zip.write(path)
# zip.close() #something happen is better to use try or with method:

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("Chapter8_Modules\ecommerce").rglob("**/*.*"):
#         zip.write(path)
#         print("ready")


with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo('Chapter8_Modules/ecommerce/customer/contact.py')
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
