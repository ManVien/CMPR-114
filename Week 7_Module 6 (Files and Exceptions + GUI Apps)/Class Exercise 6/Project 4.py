# Project 4 (Write Records)

def main():
    num_emps = int(input('enter the number of employee records: '))

    emp_file = open('employees.txt','w')

    for count in range (1, num_emps + 1):
        print('enter data for employee #', count)

        name = input('Name: ')
        id_num = input('ID NUMBER: ')
        dept = input('DEPARTMENT: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

    emp_file.close()
    print('recorded')

main()