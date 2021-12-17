# 1 Variables
import math
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(students_count)


# 2 Variables name
# Variables Names are descriptives and Meaningfull
# lower case for names
# Undersquare for separating the words, spaces is not alowed
# space before equal sign

# 3 Strings
course = "Python Programming"
message = """
 Mesaj lung,
 care include si 
 paragrafe pe mai multe
 randuri

"""

# function is a reusable piece of code to performe vorous tasks
print(len(course))
course[0]  # index of a string start with 0
print(course[0])
# negative index will overflow the string starting the count from the end
print(course[-1])
# Slicing  strings
print(course[0:3])
# without second index slicing will go to end of the string
print(course[5:])
# without first index we will get spacified number of characters from the begin
print(course[:5])
# Without both indexes we will get a coppy of the entire string
print(course[:])

# 4 Escape Sequences
# \"
# \'
# \\
# \n  - new line
course = "Python \\ Programming 2"
print(course)

# 5 Formatted strings
first = 'Mosh'
last = 'Hamedani'
full = first + " " + last
print(full)

formatted_full = f"{first} , {last}"
print(formatted_full)

formatted_full = f"{len(first)} + {2+2}"
print(formatted_full)

# 6 String Methods

course = "  Python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())  # remove white space from the begining and from the end
# there is availble also .lstrip() and also .rstrip()

# find a substring
print(course.find("pro"))  # Case sensitive
# Replace a character or a substring
print(course.replace("m", "W"))

# check if containe with 'in' /'not in' operator
print("pro" in course)
print("swift" not in course)

# 7 numners
x = 1  # integger
x = 1.1  # float
x = 1 + 2j  # complex numbers : a + bi

# Standard operations
# additions
print(10 + 3)
# substrations
print(10 - 3)
# multiplication
print(10 * 3)
# division
print(10 / 3)  # floating number
print(10 // 3)  # return integer part
# modulus
print(10 % 3)  # reminder of division
# Exponent
print(10 ** 3)  # left to the power of right

# Augmented asignament oparator
x = 10
x = x + 3
x += 3  # incresa with 3


# * working with numbers

# useful built-in functions
print(round(2.9))
print(abs(-2.9))

# importing math module
print(math.ceil(2.2))
# google : python 3 math module

print(math.factorial(3))

# 9 Type Conversion

# x = input("x: ")
# print((type(x)))
# y = int(x) + 1
# print(f"X:{x}, y: {y}")

# conversion functions
# int(x)
# float(x)
# bool(x)

# str(x)

# Falsy --> converted to bool will return false.
# ""
# 0
# None
print(bool(""))
print(bool(0))
print(bool(None))
# True
print(bool(1))
print(bool("aaaa"))
