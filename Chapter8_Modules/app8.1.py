# press control + space to get all methods
import ecommerce.shopping.sales
import sys
from ecommerce.shopping.sales import calc_shipping, calc_tax

calc_shipping()
calc_tax()

# Import could be done for all but not recomended
# from sales import *

# could be imported entire modul as an object
ecommerce.sales.calc_tax()
ecommerce.sales.calc_shipping()

# 3 - Module search path
#  import sales
# import sys
ecommerce.sales.py
print(sys.path)
