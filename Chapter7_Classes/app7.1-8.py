# 1 Classes
# Class \: blueprint for creating new objects
# Object: instance of class

#Class: Human
# Objects: John, Mary, Jack

# 2 Creating Classes


class MyPoint:  # Classes naming Use Pascal Notation
    def draw(self):  # all functions inside clss should contain at least one parameter named by convention 'self'
        print("draw")


# Creat an instance o class
point = MyPoint()
# Check the type of the object
print(type(point))

#  Check if one object is instance of a class
print(isinstance(point, MyPoint))
print(isinstance(point, int))

#3 - Constructors


class Point:
    default_color = "red"  # Class level atribut

    def __init__(self, x, y):  # From Lesson 3
        self.x = x  # atrinutes
        self.y = y  # atributes

    @classmethod     # from leson 5
    def zero(cls):
        return cls(0, 0)

    def __str__(self):  # from Lesson 6
        return f"Point ({self.x}, {self.y})"

    def __eq__(self, other):              # from lesson 7
        return (self.x == other.x) and (self.y == other.y)

    def __gt__(self, other):               # from lesson 7
        return (self.x > other.x) and (self.y > other.y)

    def __add__(self, other):              # from lesson 8
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):              # from lesson 8
        return Point(self.x-other.x, self.y-other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(10, 20)
point.draw()

# 4 Class vs Instance Attributes

Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)  # print class level atribut via instances
print(Point.default_color)   # print class level atribut via class name.
point.draw()

another = Point(3, 4)  # instance atributes provided by paranmeters
another.draw()
print(another.default_color)  # print class atribut

# class atributes

# 5 - Class vs Instance Methods

# Define a factory method to create an objects with some initial/default values.
# point = Point(0, 0)
point = Point.zero()
point.draw()

# 6 _ Magic Methods g0ogle
# google : python magic methods
# https://rszalski.github.io/magicmethods/

# If we want to print an object
# adding __str__ magic method, will convert to string the point object
print(point)
print(point)  # now printing the object will show the string version.
# accoreding the implemented __str__ magic method
print(str(point))  # same result


# 7 - Comparing Objects
point = Point(10, 20)
other = Point(1, 2)
# return False because it is comparing the references of the two pbjects, they are different.
print(point == other)

# using comparison magic method:
# __eq__ -  testing equality
# __ne__ - not equal
# __lt__ - less then

# after implementation of the __eq__ , comparison operator == should works

# comparing if is greater __gt__
# initialy TypeError: '>=' not supported between instances of 'Point' and 'Point'
print(point > other)
print(point < other)  # if __gt__ is defined 'less then is' __lt__ already created

# 8 - Performing Arithmetic Operations

# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
combined = point + other
print(combined)
# Numeric magic methods? Normal arithmetic operators :__add__, __sub__
print(point - other)
