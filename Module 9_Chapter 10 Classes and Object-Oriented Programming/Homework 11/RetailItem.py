# RetailItem Class
class RetailItem:
    # The __init__ method initializes the attributes
    def __init__(self, desc, units, price):
        self.__description = desc
        self.__units = units
        self.__price = price

    # mutator method
    def set_description(self, desc):
        self.__description = desc
     
    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    # accessor method
    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

    def __str__(self):
        return self.__description + "\t\t\t\t" + str(self.__units) + "\t\t" + str(self.__price)

