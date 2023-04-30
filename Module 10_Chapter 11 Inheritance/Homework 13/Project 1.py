# ShiftSupervisor class
# This program demonstrates an instance of the ShiftSupervisor class.

import employee

def main():
    
    name = input('Enter the shift supervisor name: ')
    emp_num = int(input('Enter the shift supervisor ID number: '))
    salary = float(input('Enter the annual salary: '))
    bonus = float(input('Enter the annual production bonus: '))

    shiftSupervisor = employee.ShiftSupervisor(name, emp_num, salary, bonus)
    print()

    # display the data
    print('Shift Supervisor Name:', shiftSupervisor.get_name())
    print('Shift Supervisor ID Number:', shiftSupervisor.get_employee_number())
    print('Shift Supervisor Annual Salary: $', shiftSupervisor.get_annual_salary())
    print('Shift Supervisor Annual Bonus: $', shiftSupervisor.get_annual_bonus())

    print()
   
main()