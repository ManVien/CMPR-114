# Automobile Costs
# This program asks the user to enter the monthly costs 
# from expenses incurred from operating automobile: 
# loan payment, insurance, gas, oil, tires, and maintenance.
# Then display the total monthly cost of these expenses, 
# and the total annual cost of these expenses.

def main():
    loan, insurance, gas, oil, tires, maintenance = get_input()
    total_monthly, total_annual = calculate_cost(loan, insurance, gas, oil, tires, maintenance)
    display_cost(total_monthly, total_annual)
   
def get_input():
    # Get monthly loan payment.
    loan_payment = float(input('Enter monthly loan payment: $'))

    # Get monthly insurance cost.
    insurance_cost = float(input('Enter monthly insurance cost: $'))

    # Get monthly gas cost.
    gas_cost = float(input('Enter monthly gas cost: $'))

    # Get monthly oil cost.
    oil_cost = float(input('Enter monthly oil cost: $'))

    # Get monthly tires cost.
    tires_cost = float(input('Enter monthly tires cost: $'))

    # Get monthly maintenance cost.
    maintenance_cost = float(input('Enter monthly maintenance cost: $'))

    return loan_payment, insurance_cost, gas_cost, oil_cost, tires_cost, maintenance_cost

def calculate_cost(loan, insurance, gas, oil, tires, maintenance):
    total_monthly_cost = 0.0
    total_annual_cost = 0.0

    # Calculate the total monthly cost of these expenses.
    total_monthly_cost = (loan + insurance + gas + 
                          oil + tires + maintenance)
    
    # Calculate the total annual cost of these expenses.
    total_annual_cost = total_monthly_cost * 12

    return total_monthly_cost, total_annual_cost

def display_cost(total_monthly, total_annual):
    # Display the total monthly cost and
    # the total annual cost of these expenses.
    print(f'The total monthly cost is ${total_monthly:,.2f}.\n'
          f'The total annual cost is ${total_annual:,.2f}.')

# Call the main function.
main()
