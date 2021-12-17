# 1 Defining Functions

def greet():
    print("Hi there")
    print("Welcome aboard")


greet()
# 2 Arguments


def greet_wth_args(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet_wth_args("Mosh", "Hamedani")
# 3 Types of Fumctions


def function_name(name):
    print(f"Hi {name}")

    # Two types of functions:
    # 1- Functions that performe a task
    # 2-
    #
    # Return a avalue


def get_greetings(name):
    return (f"Hi {name}")


message = get_greetings("Mosh")
print(message)

# file = open("content.txt", "w")
# file.write(message)

# 4 Keywords Arguments


def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

# Simplying code
print(increment(2, 1))

# making code readable by using key words arguments

print(increment(2, by=1))
# 5 - Default Arguments


# defining the default/optional parameters should come after the required parameters
def increment_second(number, by=1):
    return number + by


print(increment_second(2))
print(increment_second(2, by=5))

#6 - xargs


def multiply(x, y):
    return x*y


print(multiply(2, 3))

# multiply(2, 3, 4, 5) not working


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply(2, 3, 4, 5))

#8 - xxargs


def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=1, name="John", age=22)

#8 - Scope

message = "a"  # global variables


def greet_a(name):  # name - local variable
    message = "b"  # Local variable with the same name like global, but different


def greet_b(name):
    global message  # calling  global variable
    message = "c"


# print(name)  # name not defined out of the function

# 9 Debugging

# when start first time the debugging moe is created the launch.json file
# watching points added with F9
# step over F10
# step in F11
# step out  Alt-F11

# 10 VS Code Code Tricks - Windows
# moving cursor tthe and or begining of the line with Home and End Key (Fn + -->)
# to move cursor begining of the file use Ctrl+ Home or Ctrl+ End for moving to the end of file.
# Moving one line with Alt + Up or Alt Down
# Duplicate: Shift+Alt+Down
# Convert to coment : Ctrl+ /
# type a name with intelisense help
