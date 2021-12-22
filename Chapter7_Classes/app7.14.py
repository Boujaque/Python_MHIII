# 14 - Method Overriding
class Animal:
    def __init__(self):
        self.age = 1
        print("Animal Constructor")

    def eat(self):
        self.age = 1
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2
        print("Mammal Constructor")

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)   # this m.age not defined because was overrided
print(m.weight)
