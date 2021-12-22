#4 - Packages
# create a subfolder ecommerce where will be located the sales modul
# because the files theat are importing sales module canot find it anymore
# needs to ad __init__.py

# importing ths sales modul shoul containe also the package name:
# import ecommerce.sales

# ecommerce.sales.calc_tax()
# to avoid using the entire path for the package is better to import direct the methods
# from ecommerce.sales import calc_tax,calc_shipping

# oher method is to imports the sales module as object and to call its methods
from ecommerce import sales

sales.calc_shipping()
