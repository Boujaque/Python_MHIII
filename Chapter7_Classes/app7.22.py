# 22- Data Classes

# from collection import namedtuple


from typing import NamedTuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # false because are stored in different adress location
print(id(p1))
print(id(p2))

# data type calsses that have no methods only hold data's it is to complicate to iplement
# all methods for number and data
# easier is to implement namedtuple : from typing import NamedTuple (diferit de curs)

# Point = NamedTuple("Point", ("x", "y"))
# Point = NamedTuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)

# Named tuple is imutable canot be modified
p1.x = 10
