# This program creates an object of the ProductionWorker class and 
# prompts the user to enter data for each of the object’s data attributes. 
# Store the data in the object, then use the object’s accessor methods to retrieve it 
# and display it on the screen.
import employee

def main():

    name = input('Enter the employee name: ')
    emp_num = int(input('Enter the employee number: '))
    shift_num = int(input('Enter the shift number: '))
    pay_rate = float(input('Enter the hourly pay rate: '))

    worker = employee.ProductionWorker(name, emp_num, shift_num, pay_rate)

    print("\n")
   
    # display the data
    print('Employee Name: ', worker.get_name())
    print('Employee Number: ', worker.get_employee_number())
    print(worker.get_shift_number())
    print('Hourly pay rate: ', worker.get_pay_rate())
    print("\n")
   
main()