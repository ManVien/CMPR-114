# Monthly Sales Tax
# This program asks the user to enter the total sales for 
# the month, calculates, and displays the amount of county 
# sales tax, the amount of state sales tax, and the total
# sale tax. 

# Constant variables
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

def main():
    # Get the total sales for the month from the user.
    sales = float(input('Enter the total sales for the month: $'))
    # Call the show_sales_tax function.
    show_sales_tax(sales)

# The show_sales_tax function calculates and displays 
# the amount of county sales tax, state sales tax, 
# and total sales tax (county plus state).
def show_sales_tax(sales):
    county_sales_tax = sales * COUNTY_TAX_RATE
    state_sales_tax = sales * STATE_TAX_RATE
    total_sales_tax = county_sales_tax + state_sales_tax

    print(f'\nThe amount of county sales tax is ${county_sales_tax:,.2f}.')
    print(f'The amount of state sales tax is ${state_sales_tax:,.2f}.')
    print(f'The total sales tax is ${total_sales_tax:,.2f}.\n')

# Call the main function.
main()


