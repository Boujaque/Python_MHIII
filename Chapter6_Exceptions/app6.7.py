# 7 - Cost of exceptions

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0 : 
        raise ValueError("Age Cannot be zero or less") # google: python 3 built in exceptions
    return 10 / age

try:        
    calculate_xfactor(-1)
except ValueError as error:
    #print(error) 
    pass
"""
print("First code=", timeit(code1, number=10000))

code2 = """
def calculate_xfactor(age):
    if age <= 0 : 
        return None
    return 10 / age
    
xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass   
"""

print("Second code=", timeit(code2, number=10000))
# code 2 is 4 times faster
# raise exceptions only if needed.
