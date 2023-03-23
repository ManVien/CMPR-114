# Continuing with project 4, read the content of the employees.txt file

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
    print('recorded.\n')

main()

def read():
    # Open a file named employees.txt.
    infile = open('employees.txt','r') # reading

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    print(file_contents)

read()
