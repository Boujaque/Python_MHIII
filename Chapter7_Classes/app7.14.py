# 14 - Method Overriding
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        self.age = 1
        print("eat")

# Mamal : child, Sub


class Mammal(Animal):
    #  def eat(self):   # is duplicated
    #     print("eat")

    def walk(self):
        print("walk")


class Fish(Animal):
    # def eat(self):   # is duplicated
    #     print("eat")

    def swim(self):
        print("swim")
