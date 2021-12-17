# L1 Coparison Operators
print(10 > 3)
10 < 20
10 >= 3
10 <= 20
# Equal Operator
10 == 10  # True
10 == "10"  # False
# Not Equal Operator
10 != "10"

# Using Comparison operators with strings
"bag" > "apple"  # True
"bag" == "BAG"  # False
# Characters numeric respresentation
print(ord("b"))  # 98
print(ord("B"))  # 66

# L2 Conditional statements

temperature = 25
if temperature > 30:
    print("it's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("it's cold")
print("If block closed")

# Ternary operator
age = 22
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Logical Operators
# and or not

high_income = True
good_credit = False
student = False


if high_income and good_credit:
    print("Is eligible")
else:
    print("not eligible")

print("*******************")

if high_income or good_credit:
    print("Is eligible")
else:
    print("not eligible")

print("*******************")
if not student:
    print("Is eligible")
else:
    print("not eligible")

print("*******************")
if (high_income or good_credit) and not student:
    print("Is eligible")
else:
    print("not eligible")

# 5 Short Circuit Evaluation

if high_income and good_credit and student:  # stops when find one false element => False
    print("eligible")

if high_income or good_credit or student:  # stops when find one True element => True
    print("eligible")

# Chaining Comparison Operators

# age should be between 18 and 65
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")

# 7 Quiz
print("7 Quiz  :")
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
# 8 For Loops
print("8 For Loops")
for number in range(3):
    print("attempt", number+1, (number+1)*".")
# range from 1 to 4
for number in range(1, 4):
    print("attempt", number, number*".")
# adding steps
for number in range(1, 10, 2):
    print("attempt", number, number*".")

# For...Else
print("For...Else    :")
successful = False
for number in range(1, 4):
    print("attempt", number, number*".")
    if successful:
        print("Successful")
        break
else:
    print("attempted 3 times and failed")

# Nested Loops
print("Nested Loops    :")
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterables
print(type(5))
print(type(range(5)))
# Range is iterable and could be tereted  during for ..in loop
# String is also iterable.
# Range iteration
for x in range(5):
    print(x)
# String iteration
for x in "Python":
    print(x)
# List iteration
for x in [1, 2, 3, 4]:
    print(x)

# While Loop

number = 100
while number > 0:
    print(number)
    # number = number // 2
    number //= 2

# example
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# Infinite Loop
# command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() != "quit":
        break

    # 14 Exercise
    print("Exercise   :")
    count = 0
    for number in range(1, 10):
        if number % 2:
            print(number)
            count += 1
    else:
        print(f"We have {count} even numbers")
