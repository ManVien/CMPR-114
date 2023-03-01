# Project #2
# A program that will ask to enter the sales with commission 
# by using the while loop.

# Create a variable to control the loop.
keep_going = 'y'

# Calculate a series of commissions.
while keep_going == 'y':
# Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

# Calculate the commission.
# make sure to indent this line
    commission = sales * comm_rate 

# Display the commission.
# make sure to indent this line
    print(f'The commission is ${commission:,.2f}.') 

# See if the user wants to do another one.
# make sure to indent this line
    keep_going = input('Do you want to calculate another ' 
                       + 'commission (Enter y for yes): ')

