#1 - Exceptions
# code errors
numbers = [1, 2]
# print(numbers[3])

# wrong input from user
# age = int(input("Age: "))

# 2 Handling Exceptions
try:
    age = int(input("Age: "))
except ValueError as ex:  # define a variable that wil containe the exception
    # code is done in case of an exception
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")  # code is done in case of no exception
print("execution continues.")  # code is done in any case

# 3 - Handling Different Exceptions

try:
    age = int(input("Age: "))  # Throw ValueError exception
    xfactor = 10 / age  # Throw division by zero exception
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     print("Age Cannot be zero")
else:
    print("No exceptions were thrown")

# 4 Cleaning Up
# working with external resurces  (Files, data base, etc)
# we need to release them after usage.

try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    # file.close() # in case of  an exception this line will not be executed
    # file will remain open
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
    # file.close() # in order to close in case of exception
else:
    print("No exceptions were thrown")
    # file.close() # in order to close in case of not exception
finally:
    file.close()  # is executed in both cases

# 5 - The with Statement

try:
    with open("app.py") as file, open("another_file.txt") as target:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")
# finally: # no need finaly clause because with is prepared to close the opened resources
    # if thei have 'context management protocol' containing __enter__, __exit__
    # file.close()

# 6 - Raising Exceptions


def calculate_xfactor(age):
    if age <= 0:
        # google: python 3 built in exceptions
        raise ValueError("Age Cannot be zero or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
