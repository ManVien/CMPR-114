# vehicles
class Automobiles:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        #self.__doors = doors

    # these are the mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    #def set_doors(self, doors):
        #self.__doors = doors

    # these are the accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    #def get_doors(self):
        #return self.__doors

class Truck(Automobiles):
    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)

class SUV(Automobiles):
    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)

class Electric(Automobiles):
    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)