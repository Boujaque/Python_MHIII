#12 - Inheritance
# Animal: Parent, base
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


dog = Mammal()
dog.eat()
dog.walk()
print(dog.age)

shark = Fish()
shark.eat()
shark.swim()
print(shark.age)


# 13 The Object Class

m = Mammal()
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))
o = object()
# m.  contains method inherited from o.

# check if a class is a subclass
print("****subclass check: *******************")
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
print(issubclass(Animal, object))
