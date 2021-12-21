# Daya Structures:
# -Lists
# -Touples
# -Dictionaries

# 1 Lists
# - not need to be the same type elements
from sys import getsizeof
from array import array
from collections import deque
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

# sorting lists of complex items

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

items.sort()
print(items)


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# 8 Lambda Functions
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
# define lambda functions

items.sort(key=lambda item: item[1])
print(items)

# 9 Map Function

# Transforming the list of touples in a list a numbers (prices)
# explicit view
prices = []
for item in items:
    prices.append(item[1])
print(prices)

# Lambda function
x = map(lambda item: item[1], items)
for item in x:
    print(item)

# Simplification
prices = list(map(lambda item: item[1], items))
print(prices)


# 10 Filter Function

x = filter(lambda item: item[1] >= 10, items)
print(x)  # result a filter object that is iterable and can be converted to alist

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# 11 - List Comprehensions
# replace the map and filter lists but is cleaner and more easy to use:

# Maping
# [expresion for item in items]
prices_compr = [item[1] for item in items]
print(prices_compr)
# Filtering
# [expresion for item in items if item condition]
filtered_compr = [item[0] for item in items if item[1] >= 10]
print(filtered_compr)

# 12 Zip function
# combine two list into a list of touples that combine the their elements.

list1 = [1, 2, 3]
list2 = [10, 20, 30]

list_combined = [(1, 10), (2, 10), (3, 30)]

print(zip(list1, list2))  # rezult an iterable object
# can be converted to a list:
list_zipped = list(zip("abc", list1, list2))
print(list_zipped)

# 13- Stacks
# LIFO - Last In- First Out

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
# Use pop() to get last item
last = browsing_session.pop()
print(last)
print(browsing_session)
# to see tha last item in the list (peek function in java)
print("redirect", browsing_session[-1])
# in order to check if list is not empty
if not browsing_session:
    print("disable the button")

# 14 Queues
# FIFO - First In - First Out


queue = deque([])  # deque from collections
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# return first item
first = queue.popleft()
print(first)
print(queue)
# check the queue if empty
if not queue:
    print("empty")
# 15 Tuples
# read only list- cannot chnbged inside elements,
# ore change the order inside tuples.
point = (1, 2)  # Tuple with paranthesis
print(type(point))
point = 1, 2  # tuple without paranthesis
print(type(point))
point = 1,  # tuple without one elemet but with comma
print(type(point))
point = ()  # empty touple
print(type(point))

# Concatenation
point = (1, 2) + (3, 4)
print(point)
# Mutiplication of a tuple
point = (1, 2) * 3
print(point)
# Convert a list to a tuple
point = tuple([1, 2])
print(point)
# Casting a string to a tuple
point = tuple("Hello World")
print(point)

# Access tuple items
point = (1, 2, 3)
print(point[0])
print(point[0:2])
# unpacking a tuple
x, y, z = point
print(x)
print(y)
# check if contain a value
if 10 in point:
    print("exists")
else:
    print("not exists")
# Tuple is imutable elements canot be changed
# point[0] = 10 # return error TypeError: 'tuple' object does not support item assignment
# 16 Swapping variables
x = 10
y = 11
x, y = y, x
print("x=", x, ", y=", y)
# 17 Arrays
[1, 2, 3]

# first argument is 'typecode' ( search in google)
numbers = array("i", [1, 2, 3])

# adding element to the end
numbers.append(4)
print(numbers)

# inserting to position index
numbers.insert(2, 5)  # Insert a new item v into the array before position i.
print(numbers)

# pop elements

last = numbers.pop()
print(last)
print(numbers)
last = numbers.pop(2)
print(last)
print(numbers)

#  remove elements
numbers.remove(3)
print(numbers)

# return by index
print(numbers[0])

# if we want to change one element we need to provide the same tipe
numbers[0] = 10

print(numbers)

# 18 Sets
# unordere colections, has no index
# list of unique items
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)

# defining a set literal with { }
second = {1, 4}

# add to a set
second.add(5)
print(second)

# removing item from set
second.remove(4)
print(second)
# check the number of items (length)
print(len(second))

# operations with sets
# reunion
first = uniques
print(first | second)

# Intersection
print(first & second)

# Diference
print(first - second)

# Simetric diference
print(first ^ second)

# first[0] - will return error
# could be chcked if a value exists in a set.
if 1 in first:
    print("yes")

# 19 - Dictionaries:
# colection of Key-Value pairs
# mapping a key to a value
# phonne book - dictionary
# name --> contact details  (mapping contact details based on the name)
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point)
print(point["x"])

# change a value of an key
point["x"] = 10
point["z"] = 20
print(point)

# checking the key
# if we ask a key thet is not exist we receive an error
# we need to check yhe existance before

if "a" in point:
    print(point["a"])

# could be used also the get() method to return the value for a key,
# in case that key not exist will return none.
print(point.get("a"))
# get can return a default value
print(point.get("a", 0))
print(point.get("a", "not contained"))

# Delete Item
del point["x"]
print(point)

# iterate over dictionary

for key in point:
    print(key)

for key in point:
    print(key, point[key])

 # unpack dictionary

for x in point.items():
    print(x)

# unpack tuples results
for key, value in point.items():
    print(key, value)

# 20 - Dictionaries comprehension

values = []
for x in range(5):
    values.append(x*2)

print(values)

# we can use mapping ore list comprehension
# [expresion for item in items]
values = [x*2 for x in range(6)]
print(values)
# creating a set:
set_values = {x*2 for x in range(6)}
print(set_values)
# Creating a dictionary based on key value pairs
dict_values = {x: x*2 for x in range(6)}
print(dict_values)

# Creating a tuple with comprehension method
# is not possible , will rezult an object generator
tuple_values = (x*2 for x in range(6))
print(tuple_values)
# <generator object <genexpr> at 0x000001CFD7E320B0>

# 21 Generator expresions
values = [x * 2 for x in range(10)]
for x in values:
    print(x)
# Object generators are iterable
# generator objects creation (same with tuple creation)
values = (x * 2 for x in range(10))
print(values)
for x in values:
    print(x)
# Check the size of the generator object
set_values = {x*2 for x in range(10000)}
print("set:", getsizeof(set_values))
list_values = {x*2 for x in range(10000)}
print("list:", getsizeof(list_values))
dict_values = {x: x*2 for x in range(10000)}
print("dict:", getsizeof(dict_values))
gen_values = (x * 2 for x in range(10000))
print("gen:", getsizeof(gen_values))
# print(len(gen_values)) # generate eror: TypeError: object of type 'generator' has no len()

# 22 - Unpacking operator
numbers = [1, 2, 3]
print(*numbers)  # similar cu spred operator (...) in javascript
print(1, 2, 3)
# unpacking operator on iterables

values = list(range(5))
print(values)
values = [*range(5), *"hello"]
print(values)
# combining lists
first = [1, 2]
second = [3]
values = [*first, 'a', *second, *"hello"]
print(values)
# combining dictionaries
first = {"x": 1}
second = {"x": 10, "y": 3}
combined = {**first, **second, "z": 1}
print(combined)
