# 10 - Working with DateTime
from datetime import datetime
import time

dt = datetime(2018, 12, 23)
print(dt)
dt1 = datetime.now()
print(dt1)
# string parsing to dattetime
dt2 = datetime.strptime("2018/10/15", "%Y/%m/%d")
# documentation at python 3 datetime %Y 4 digits year
print(dt2)
# convert timestamp  to datetime
dt4 = datetime.fromtimestamp(time.time())
print(dt4)

# Formating the dattime print:
print(f"{dt.year}/{dt.month}")
print(f"{dt1.year}/{dt1.month}")
print(f"{dt2.year}/{dt2.month}")
print(f"{dt4.year}/{dt4.month}/{dt4.day}")

# conceriting datetime object into a string
print(dt.strftime("%d/%m/%Y"))
print(dt4.strftime("%d/%m/%Y"))
# Comparison
print(dt1 > dt2)

