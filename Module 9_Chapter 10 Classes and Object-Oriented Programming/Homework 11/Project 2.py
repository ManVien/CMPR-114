# The program should store the data in the three objects, 
# then display the data for each employee on the screen.

import Employee

def main():

    # Create the instance of the Employee class.
    employee1 = Employee.Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')

    employee2 = Employee.Employee('Mark Jones', 39119, 'IT', 'Programmer')

    employee3 = Employee.Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    # Display the data that was entered.
    print('\nHere is the data for each employee:')
    print('Name\t\tID Number\tDepartment\tJob Title')
    print(employee1)

    print(employee2.get_name() + "\t" + str(employee2.get_id_number()) + "\t\t" +
          employee2.get_department() + "\t\t" + employee2.get_job_title())

    print(employee3)
    print()

main()