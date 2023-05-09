# the Employee class keeps data attributes for the following pieces of information: employee name and employee number.
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
    
# ProductionWorker is a subclass of the Employee class.
# The ProductionWorker class should keep data attributes for the following information:
# shift number (an integer, such as 1, 2, or 3) and hourly pay rate.
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
            print('Shift 1: Day shift')
        elif self.__shift_number == 2:
            print('Shift 2: Night shift')
        else:
            print('That is not a valid shift')

    def get_pay_rate(self):
        return self.__pay_rate

# This program creates a list of 3 objects of the ProductionWorker.  
# Traverse the list and print out the content of the 3 ProductionWorker objects on the screen.

def main():

    workers = [ProductionWorker("Man Vien", "111", 1, 19.5),
               ProductionWorker("Kevin Smith", "222", 2, 22.5),
               ProductionWorker("JT Tran", "333", 1, 16.5)]
   
    # display the data
    for worker in workers:
        print('Employee Name:', worker.get_name())
        print('Employee Number:', worker.get_employee_number())
        worker.get_shift_number()
        print('Hourly pay rate: $', worker.get_pay_rate())
        print()
   
main()