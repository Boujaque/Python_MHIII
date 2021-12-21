
#11 - Properties

# non pythonic solution for setter and getters like in java


class Product:
    def __init__(self, price):
        # self.__price = price
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative.")
        self.__price = value

    def __str__(self):
        return f"Produs pret ({self.__price})"


produs1 = Product(50)
print(produs1)

# using properties object for define setters and getters


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative.")
        self.__price = value

    # property function has 4 atributes: fget, fset, fdel, doc
    price = property(get_price, set_price)


produs2 = Product(50)
# print(produs1.get_price)
produs2.price = 30
print(produs2.price)
# produs2.   but Get_price and set_price are visible in order to not aheve them


class Product:
    def __init__(self, price):
        self.price = price

    @property          # define price getter
    def price(self):
        return self.__price

    @price.setter       # define price setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative.")
        self.__price = value


produs3 = Product(50)
# print(produs1.get_price)
# without setter class is read only and reseting the price will throw an error
produs3.price = 40
print(produs3.price)
