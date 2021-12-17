# Daya Structures:
# -Lists
# -Touples
# -Dictionaries

# 1 Lists
# - not need to be the same type elements
letters = ["a", "b", "c"]
boolean = [True, False, True, True]
numbers = [1, 13, 45, 67]
matrix = [[1, 2], [23, 5, 8], [1]]
zeros = [0]*10

# Concatenation of lists
combined = zeros + letters

print(combined)

numbers = list(range(20))  # first 20 numbers, 20 not included
print(numbers)
chars = list("Hello World")
print(chars)
# Length function
print(len(chars))

# Accesing Items

print(letters[0])  # first item
print(letters[-1])  # first from the list

# Change item in a list
letters[1] = "B"

print(letters)

# add to a list
letters += "d"

print(letters)

# Slicing a list
print(letters[0:3])  # return a list with fisrt 3 characters
print(letters[:3])  # return a new list all elements to the third
print(letters[1:])  # return a new list starting from mentioned index
print(letters[:])  # returna coppy of the list
print(letters[::2])  # returna every second element in the original list
print(letters[::-1])  # return all items in original list in revers order.

# 3 - List Unpacking
#  Unpack  - split a list into multiple variables

numbers = [1, 2, 3]
a = numbers[0]
b = numbers[1]
c = numbers[2]

# simplier way to unpack
first, second, third = numbers  # numbers of elements from left should be equal
# with the number of elements from the list.
print(first, second, third)
# if we are interested only on few items from the list
numbers = [5, 5, 3, 4, 4, 4, 9]
# first, second, third = numbers will retuprint(first, second, third)rn error
first, second,  *other = numbers
print(first, second, third)
# rest of ellemnt are storred in the list 'other'
print(other)
first, *other, last = numbers
print(first, last)

# 4 Looping over list
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

for letter in enumerate(letters):  # return a touple
    print(letter)

# printing contrent of the touple:

for letter in enumerate(letters):
    print(letter[0], letter[1])
# 5 Adding or Removing items to a list

# add
# to the end -  .append() methods
letters.append("e")
print(letters)

# add item to a specific position : .insert()
letters.insert(3, "f")
print(letters)

# Remove item - to the end
print(letters.pop())  # return the last element
print(letters)
print(letters.pop(1))  # remove item at given index
print(letters)
# remove item when we don't know the index
letters.remove("c")  # remove first occurence of letter 'c'
print(letters)
# refiling the list


def refill():
    letters_add = ("a", "b", "c", "d", "e", "f")
    index = 0
    letters.clear()
    for letter in letters_add:
        letters.insert(index, letter)
        index += 1
    return letters


letters = refill()
print(letters)

# Delete items and range of items
del letters[0:3]
print(letters)

# remove all items from the list use the clear method)
letters = refill()
print(letters)
letters.clear()
print(letters)
# 6 - Finding items in a list
# return the index of item from the list
letters = refill()
print(letters)
print(letters.index("d"))
# print(letters.index("m")) will through an exception
# needs to checked the existence before
if "m" in letters:
    print(letters.index("m"))

# count() method - return the number of occurences of the given item in the list
print(letters.count("d"))
# 7 Sorting lists
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

# sorting revers order  using revers parameters
numbers.sort(reverse=True)
print(numbers)
# will not modify original list
sorted_numbers = sorted(numbers)
print(sorted(numbers))
print(sorted(numbers, reverse=True))
