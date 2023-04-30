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

# The ShiftSupervisor class is a subclass of the Employee class
class ShiftSupervisor(Employee):
    def __init__(self, name, employee_number, salary, bonus):
        super().__init__(name, employee_number)
        self.__annual_salary = salary
        self.__annual_bonus = bonus

    def set_annual_salary(self, salary):
        self.__annual_salary = salary

    def set_annual_bonus(self, bonus):
        self.__annual_bonus = bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus