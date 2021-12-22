# 15 Multilevel Inheritance
class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chiccken(Bird):  # Chicken not fly but inherit
    pass

# 16 - Multiple Inheritance


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


# First Base clase will transfer the Greet Mtehod.
class Manager(Employee, Person):
    pass


# First Base clase will transfer the Greet Mtehod.
class Manager(Person, Employee):
    pass


manager = Manager()
manager.greet()  # Employee Greet

# Good example of multiple inheritance
# if classes are independent thy can be a good base multiple for inheritance


class Swimmer:
    def swim(self):
        print("Swim")


class Flayer:
    def fly(self):
        print("fly")


class FlayerFish(Swimmer, Flayer):
    def __init(self):
        self.age = 1
