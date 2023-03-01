# Challenge Exercise #2
# A program that will ask the user to enter the sales with commission four times
# by using the while loop and sum the sales and commission.  

# Create a variable to control the loop.
keep_going = 1

# Initialize the accumulator variables
total_sales = 0.00
total_comm = 0.00
total_sales_and_comm = 0.00

# Calculate a series of commissions.
while keep_going < 5:
# Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

# Calculate the commission.
# make sure to indent this line
    commission = sales * comm_rate 

# Display the commission.
# make sure to indent this line
    print(f'The commission is ${commission:,.2f}.\n') 

# Sum the sales
    total_sales = total_sales + sales
# Sum the commission
    total_comm = total_comm + commission
# Sum the sales and commission
    total_sales_and_comm = total_sales + total_comm

    keep_going += 1

# Display the sum
print(f'The sum of the sales is ${total_sales:,.2f}.')
print(f'The sum of the commission is ${total_comm:,.2f}.')
print(f'The sum of the sales and commission is ${total_sales_and_comm:,.2f}.')


