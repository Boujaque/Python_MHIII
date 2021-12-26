# 12 - Generating Random Values
import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
# chose un number of options from an array
print(random.choices([1, 2, 3, 4], k=2))
# useful when we want to generate  a password
print(random.choices("abcdefghijklmnopqrstuvWxz", k=4))
# returning a string:
print("".join(random.choices("abcdefghijklmnopqrstuvWxz", k=8)))

# better solution
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

print(string.digits)

print("".join(random.choices(string.ascii_letters+string.digits, k=8)))

# shuffling an array
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)

