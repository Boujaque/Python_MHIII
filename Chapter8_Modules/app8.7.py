# 7 The dir function

from ecommerce.shopping import sales

sales.calc_shipping()

print(dir(sales))  # will print all methods available in in the module:
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'calc_shipping', 'calc_tax',
# 'contact']

print(sales.__name__)
print(sales.__package__)
print(sales.__file__)
