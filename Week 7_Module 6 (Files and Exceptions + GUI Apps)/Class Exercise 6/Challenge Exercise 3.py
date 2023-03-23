# continuing from project #3, write a program that will ask the user to enter
# the sales with salary. If the total sales are greater than 1000, add 10% commission
# to the salary. Write and read the data using the print statement.

def sales():

    # Initialize an accumulator to 0.0.
    total_sales = 0.0

    # Get the salary from user
    salary = int(input('enter the salary: $'))
    # Get the days of sales from user
    num_days = int(input('enter the days of sales: '))
    # Open the sales_and_salary.txt file in append mode.
    sales_and_salary_file = open('sales_and_salary.txt','a')
    sales_and_salary_file.write('The days of sales: ' + str(num_days) + '\n')

    for count in range(1,num_days + 1): # start with 1, and increment by 1 based on the input
        # inside of the loop because its nested after the for loop
        sales = float(input('enter the sales for day # ' + str (count) + ' : '))
        # Append the data to the file.
        sales_and_salary_file.write('The sales for day # ' + str (count) + ': ' + str(sales) + '\n')

        # Add the sales to total_sales
        total_sales += sales

    sales_and_salary_file.write(f'The total sales is {total_sales:,.2f}\n')

    # if the total sales are greater than 1000,
    # add 10% commission to the salary
    if total_sales > 1000:
        salary = 1.1 * salary 
        sales_and_salary_file.write(f'The salary after adding 10% commission is ${salary:,.2f}')
    else:
        sales_and_salary_file.write(f'The salary is ${salary:,.2f}')

    # Close the file.
    sales_and_salary_file.close()
    print('data recorded.\n')

sales()

def Read():

    sales_and_salary_file = open('sales_and_salary.txt','r')

    # Read the first line from the file
    line = sales_and_salary_file.readline()

    while line != '': # as long as an empty string is NOT returned
        # Strip the \n from the line
        line_content = line.rstrip('\n')
        # Display the record.
        print(line_content)
        # Read the next line
        line = sales_and_salary_file.readline()

    sales_and_salary_file.close()

Read()

