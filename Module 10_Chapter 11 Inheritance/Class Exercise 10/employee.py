class Employee:
    def __init__(self, name, employee_number):
        self.__name = name
        self.__employee_number = employee_number
       
    # these are the mutator methods
    def set_name(self, name):
        self.__name = name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    # these are the accessor methods
    def get_name(self):
        return self.__name

    def get_employee_number(self):
        return self.__employee_number
    
class ProductionWorker(Employee):
    def __init__(self, name, employee_number, shift_number, pay):
        
        super().__init__(name, employee_number)

        self.__shift_number = shift_number
        self.__pay_rate = pay

    # these are the mutator methods
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay_rate(self, pay):
        self.__pay_rate = pay

    # these are the accessor methods
    def get_shift_number(self):

        if self.__shift_number == 1:
            self.__shift_number = 'Day shift'
        elif self.__shift_number == 2:
            self.__shift_number = 'Night shift'
        else:
            print('That is not a valid shift')

        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate
