# a class named Person with data attributes for a person’s name, address, and telephone number. 
class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone_number = telephone

    # these are the mutator methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone_number(self, telephone):
        self.__telephone_number = telephone

    # these are the accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone_number(self):
        return self.__telephone_number

# Customer that is a subclass of the Person class
# The Customer class should have a data attribute for a customer number, and
# a Boolean data attribute indicating whether the customer wishes to be on a mailing list. 
class Customer(Person):
    def __init__(self, name, address, telephone, cust_num, on_mailing_list):
        Person.__init__(self, name, address, telephone)

        self.__customer_number = cust_num
        self.__on_mailing_list = on_mailing_list

    # these are the mutator methods
    def set_customer_number(self, cust_num):
        self.__customer_number = cust_num

    def set_on_mailing_list(self, on_mailing_list):
        self.__on_mailing_list = on_mailing_list

    # these are the accessor methods
    def get_customer_number(self):
        return self.__customer_number

    def get_on_mailing_list(self):
        if self.__on_mailing_list:
            print(f'The customer wishes to be on a mailing list.')
        else:
            print('The customer does not wish to be on a mailing list.')
        

